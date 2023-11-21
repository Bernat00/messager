
connected_users = []


class ConnectedUser:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def id_from_username(username):
        for user in connected_users:
            if user['username'] == username:
                return user

    @staticmethod
    def add_user(id, username):
        connected_users.append(ConnectedUser(id, username))

    @staticmethod
    def remove_user(id):
        for i in connected_users:
            if i.id == id:
                connected_users.remove(i)