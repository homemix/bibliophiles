from models.database import db
from flask_login import UserMixin

"""A class to represent a Users"""


class User(UserMixin,db.Model):
    """ Users Model """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    usertype_id = db.Column(db.ForeignKey('user_types.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False,
                            index=True)

    usertype = db.relationship('UserType')

    def __init__(self, username, password, email, usertype_id):
        self.username = username
        self.password = password
        self.email = email
        self.usertype_id = usertype_id

    def __repr__(self):
        """UserTypes File representation"""
        return vars(User)
