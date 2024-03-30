
class User():
    def __init__(self, id, username, encoded_password):
        self.id = id
        self.username = username
        self.encoded_password = encoded_password

    def __str__(self):
        return f"User: {self.username}"