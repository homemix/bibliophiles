from flask import Blueprint, render_template

from models.Book import Book

books = Blueprint('books', __name__)


@books.route('/')
def index():
    page_title = 'Books'
    all_books = Book.query.all()
    return render_template('books/index.html',
                           page_title=page_title, books=all_books)

