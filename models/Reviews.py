from models.database import db

"""A class to represent a reviews"""


class Reviews(db.Model):
    """ Reviews Model """
    __tablename__ = 'Reviews'
    id = db.Column(db.Integer, primary_key=True)
    ratings = db.Column(db.Integer, nullable=False)
    reviews = db.Column(db.Text(), nullable=False)
<<<<<<< HEAD
    
    books_id = db.Column(db.Integer, db.ForeignKey('Books.id'))
    books = db.relationship("Books", back_populates="reviews")

    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
=======
    books_id = db.Column(db.Integer, db.ForeignKey('UserTypes.id'))
    Reviews = db.relationship("Books", back_populates="Reviews")

    user_id = db.Column(db.Integer, db.ForeignKey('UserTypes.id'))
>>>>>>> 648a61c527909ebf4ecf9c9b75d5a83b35944ddc
    user_id = db.relationship("Users", back_populates="reviews")

    def __init__(self, ratings, reviews, books_id, user_id):
        self.books_id = books_id
        self.ratings = ratings
        self.reviews = reviews
        self.user_id = user_id

    def __repr__(self):
        return vars(Reviews)
