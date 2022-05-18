from flask import Blueprint, render_template, request, redirect, jsonify, flash

from models.Book import Book
from models.Genre import Genre
from models.database import db

from flask_login import login_required

books = Blueprint('books', __name__)

page_title = 'Books'


@books.route('/')
@login_required
def index():
    all_books = Book.query.all()
    book_genre = Genre.query.all()
    return render_template('books/index.html',
                           page_title=page_title,
                           books=all_books,
                           genres=book_genre
                           )


@books.route('/show/<int:book_id>')
@login_required
def show(book_id):
    book = Book.query.get_or_404(book_id)
    if book:
        return jsonify(book.serialize())
    else:
        flash('Book not found!', 'danger')


@books.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        published_date = request.form['published_date']
        publisher = request.form['publisher']
        genre_id = request.form['genre_id']
        new_book = Book(title=title,
                        author=author,
                        published_date=published_date,
                        publisher=publisher,
                        genre_id=int(genre_id)
                        )
        try:
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect('/books')
        except:
            flash('There was a problem adding book.', 'danger')
            return "There was a problem adding new book."
    else:
        return render_template('books/book_add_form.html')


@books.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    book_id = request.form['id']
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.published_date = request.form['published_date']
        book.publisher = request.form['publisher']
        book.genre_id = request.form['genre_id']
        try:
            db.session.commit()
            flash('Book updated successfully!', 'success')
            return redirect('/books')
        except:
            flash('There was a problem updating book.', 'danger')
            return "There was a problem updating book."
    else:
        return "There was a problem updating book."


@books.route('/delete/<int:book_id>', methods=['POST', 'GET'])
@login_required
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    try:
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully!', 'success')
        return redirect('/books')
    except:
        flash('There was a problem deleting book.', 'danger')
        return "There was a problem deleting book."
