from sqlalchemy import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chats"

    chat_id = Column("chat_id", Integer, primary_key=True, autoincrement=True)
    sender_id = Column("sender_id", Integer) # foreign
    receiver_id = Column("receiver_id", Integer) # key
    content = Column("content", Text(1024))
    timestamp = Column("timestamp", TIMESTAMP, server_default=func.now())

    def __init__(self, chat_id, sender_id, receiver_id, content, timestamp):
        self.chat_id = chat_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = timestamp


class Users(Base):
    __tablename__ = "users"

    user_id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", VARCHAR(256))
    password = Column("password", VARCHAR(256))

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password


engine = create_engine("sqlite:///mesager.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



