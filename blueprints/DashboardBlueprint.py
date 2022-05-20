from flask import Blueprint, render_template
from models.User import User
from models.Review import Review
from models.Book import Book
from models.Genre import Genre

dashboard = Blueprint('dashboard', __name__)

page_title = "Dashboard"


@dashboard.route('/')
def index():
    all_books = Book.query.count()
    all_users = User.query.count()
    all_reviews = Review.query.count()
    all_genres = Genre.query.count()
    return render_template('dashboard/index.html',
                           all_books=all_books,
                           all_users=all_users,
                           all_reviews=all_reviews,
                           all_genres=all_genres,
                           page_title=page_title)
