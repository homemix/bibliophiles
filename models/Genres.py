from models.database import db

"""A class to represent a Genres"""


class Genres(db.Model):
    """ Reviews Model """
    __tablename__ = 'Genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    books = db.relationship("Books", back_populates="Genres")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """File represention"""
        return vars(Genres)
