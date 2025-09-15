def get_weather(temp):
    if temp > 20:
        return "hot"
    else:
        return "cold"
    
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class Usermanager:
    def __init__(self):
        self.users = {}

    def add_users(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True
    
    def get_user(self, username):
        return self.users.get(username)