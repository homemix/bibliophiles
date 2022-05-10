from models.database import db

"""A class to represent a reviews"""

class Reviews(db.Models):
    """ Reviews Model """
    __tablename__ = 'Reviews'
    id = db.Column(db.Integer, primary_key=True)
    ratings = db.Column(db.Integer, nullable=False)
    reviews = db.Column(db.Text(), nullable=False)
    books_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, ratings, reviews, books_id, user_id):
        self.books_id = books_id
        self.ratings = ratings
        self.reviews = reviews
        self.user_id = user_id

    def __repr__(self):
        return vars(Reviews)
        