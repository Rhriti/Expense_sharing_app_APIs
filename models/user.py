from utils.database import get_db

class User:
    def __init__(self, email, name, mobile_number):
        self.email = email
        self.name = name
        self.mobile_number = mobile_number
    

    def save(self):
        db = get_db()
        users = db.users
        users.insert_one({
            'email': self.email,
            'name': self.name,
            'mobile_number': self.mobile_number,
        })


