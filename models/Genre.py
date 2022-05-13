from models.database import db

"""A class to represent a Genres"""


class Genre(db.Model):
    """ Genres Model """
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """File representation"""
        return vars(Genre)
