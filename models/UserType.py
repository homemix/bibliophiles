from models.database import db

"""A class to represent a User types"""


class UserType(db.Model):
    """ UserTypes Model """
    __tablename__ = 'user_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """UserTypes File representation"""
        return vars(UserType)
