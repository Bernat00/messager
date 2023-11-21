from flask import Flask, render_template, g, request, session, url_for
from flask_socketio import SocketIO, has_request_context
from db import Users, session
from users import ConnectedUser
from sqlalchemy import *

app = Flask(__name__)
socket = SocketIO()
app.config["SECRET_KEY"] = "secret"
socket.init_app(app)


# region endpoints

@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')

# endregion

# region events


@socket.on('connect')
def connect():
    print('connected!')


@socket.on('login')
def login(data):
    if data is not None:
        if data['password'] == session.scalar(select(Users.password).where(Users.username == data['username'])):
            g.user = {
                'id': request.sid,
                'username': data['username']
                # kell majd role?
            }
            print(request.sid)
            ConnectedUser.add_user(g.user['id'], g.user['username'])
            socket.emit('redirect', {'url': url_for('chat')})


@socket.on('messege')
def messege(data):
    print(request.sid)
    socket.emit('mesage', data['message'], to=ConnectedUser.id_from_username(data['recepiant']))


@socket.on('disconnect')
def disconnect():
    ConnectedUser.remove_user(request.sid)
    print('disconnected!')

# endregion


if __name__ == '__main__':
    app.run()
