import os

class Config:
    MONGO_URI = 'mongodb://localhost:27017/expense_share_app'
    SECRET_KEY = os.urandom(24)
