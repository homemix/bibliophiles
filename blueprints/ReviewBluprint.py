from flask import Blueprint, render_template
from models.Review import Review
from models.Book import Book

reviews = Blueprint('reviews', __name__)
page_title = 'Reviews'


@reviews.route('/<int:books_id>')
def index(books_id):
    all_reviews = Review.query.filter(Review.books_id == books_id).all()
    book=Book.query.get(books_id)
    return render_template('reviews/index.html',
                           page_title=page_title,
                           book=book,
                           reviews=all_reviews)
