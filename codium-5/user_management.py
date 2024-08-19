import datetime
from config import MAX_USERS


class UserManager:

    def __init__(self):
        self.users = {}

    def add_user(self, *, username, password):
        if len(self.users) >= MAX_USERS:
            return False
        if username in self.users:
            return False
        self.users[username] = {"password": password, "created_at": datetime.datetime.now()}
        return True

    def authenticate(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def get_user_info(self, username):
        return self.users.get(username, None)
