from models.database import db

""" A class to represent a book """


class Books(db.Model):
    """ Books Model """
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    published_date = db.Column(db.Date, nullable=False)
    publisher = db.Column(db.String(80), nullable=False)
    genres_id = db.Column(db.Integer, db.ForeignKey('Genres.id'))
    genres = db.relationship("Genres", back_populates="books")
    reviews = db.relationship("Reviews", back_populates="books")

    def __init__(self, title, author, genre_id, published_date, publisher):
        self.title = title
        self.author = author
        self.genre_id = genre_id
        self.published_date = published_date
        self.publisher = publisher

    def __repr__(self):
        return "<Books %r>" % self.title, self.author, self.genre_id, self.published_date, self.publisher

