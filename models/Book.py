from models.database import db

""" A class to represent a book """


class Book(db.Model):
    """ Books Model """
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    genre_id = db.Column(db.ForeignKey('genres.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    genre = db.relationship('Genre')

    def __init__(self, title, author, genre_id, published_date, publisher):
        self.title = title
        self.author = author
        self.genre_id = genre_id
        self.published_date = published_date
        self.publisher = publisher

    def __repr__(self):
        return "<Books %r>" % self.title, self.author, self.genre_id, self.published_date, self.publisher
