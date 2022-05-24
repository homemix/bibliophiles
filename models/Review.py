from models.database import db

"""A class to represent a reviews"""


class Review(db.Model):
    """ Reviews Model """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    users_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'))
    books_id = db.Column(db.ForeignKey('books.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    books = db.relationship('Book')
    user = db.relationship('User')

    def __init__(self, rating, review, users_id, books_id):
        self.rating = rating
        self.review = review
        self.users_id = users_id
        self.books_id = books_id

    def __repr__(self):
        return vars(Review)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'review': self.review,
            'users_id': self.users_id,
            'books_id': self.books_id,
            'books': self.books.serialize_reviews(),
        }
