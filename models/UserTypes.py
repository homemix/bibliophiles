from models.database import db

"""A class to represent a User types"""

class UserTypes(db.Models):
    """ UserTypes Model """
    __tablename__ = 'UserTypes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    user = db.relationship("Users", back_populates="UserTypes")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """UserTypes File represention"""
        return  vars(UserTypes)