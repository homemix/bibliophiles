from models.database import db
""" A class to represent a book """

class Books(db.Model):
    """ Books Model """
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
