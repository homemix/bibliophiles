from flask import Blueprint, render_template, request, redirect

from models.Book import Book
from models.database import db

books = Blueprint('books', __name__)

page_title = 'Books'


@books.route('/')
def index():
    all_books = Book.query.all()
    return render_template('books/index.html',
                           page_title=page_title, books=all_books)


@books.route('/<int:book_id>')
def show(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('books/show.html', page_title=page_title, book=book)


@books.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = Book(title=title, author=author)
        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new book."
    else:
        return render_template('books/create.html', page_title=page_title)
