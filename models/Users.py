from models.database import db

"""A class to represent a Users"""

class Users(db.Models):
    """ Users Model """
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text(), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False)
    UserTypes_id = db.Column(db.Integer, db.ForeignKey('UserTypes.id'))
    UserTypes = db.relationship("UserTypes", back_populates="user")
    Reviews = db.relationship("Reviews", back_populates="user_id")

    def __init__(self, user_name, password, email, UserTypes_id):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.UserTypes_id = UserTypes_id


    def __repr__(self):
        """UserTypes File represention"""
        return  vars(Users)