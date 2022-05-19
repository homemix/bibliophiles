from models.database import db

"""A class to represent a User types"""


class UserType(db.Model):
    """ UserTypes Model """
    __tablename__ = 'user_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, default=2)

    def __init__(self, name, description, user_id=2):
        self.name = name
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        """UserTypes File representation"""
        return vars(UserType)

    def serialize(self):
        """Serialize UserType"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
