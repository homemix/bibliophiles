from models.database import db

"""A class to represent a Users"""

class Users(db.Models):
    """ Users Model """
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text(), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False)
    User_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_name, password, email, User_id):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.User_id = User_id


    def __repr__(self):
        """UserTypes File represention"""
        return  vars(Users)