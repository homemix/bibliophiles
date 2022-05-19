from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Review import Review
from models.Book import Book
from models.database import db

from flask_login import login_required, current_user

reviews = Blueprint('reviews', __name__)
page_title = 'Reviews'


@reviews.route('/<int:books_id>')
@login_required
def index(books_id):
    all_reviews = Review.query.filter(Review.books_id == books_id).all()
    book = Book.query.get(books_id)
    return render_template('reviews/index.html',
                           page_title=page_title,
                           book=book,
                           books_id=books_id,
                           users_id=current_user.id,
                           reviews=all_reviews)


@reviews.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    users_id = request.form.get('users_id')
    books_id = request.form.get('books_id')
    rating = request.form.get('rating')
    review = request.form.get('review')

    # check if the review exists
    review_exists = Review.query.filter_by(users_id=users_id, books_id=books_id).first()
    if review_exists:
        flash('You have already reviewed this book', 'info')
        return redirect(url_for('reviews.index', books_id=books_id))

    new_review = Review(users_id=users_id, books_id=books_id, rating=rating, review=review)
    try:
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully', 'success')
        return redirect(url_for('reviews.index', books_id=books_id))
    except:
        flash('Review not added', 'danger')
        return redirect(url_for('reviews.index', books_id=books_id))


@reviews.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    review_id = request.form.get('reviewId')
    review = Review.query.get_or_404(review_id)
    if request.method == 'POST':
        review.rating = request.form.get('rating')
        review.review = request.form.get('review')
        try:
            db.session.commit()
            flash('Review updated successfully', 'success')
            return redirect(url_for('reviews.index', books_id=review.books_id))
        except:
            flash('Review not updated', 'danger')
            return redirect(url_for('reviews.index', books_id=review.books_id))


@reviews.route('/delete/<int:review_id>')
@login_required
def delete(review_id):
    review = Review.query.get_or_404(review_id)
    try:
        db.session.delete(review)
        db.session.commit()
        flash('Review deleted successfully', 'success')
        return redirect(url_for('reviews.index', books_id=review.books_id))
    except:
        flash('Review not deleted', 'danger')
        return redirect(url_for('reviews.index', books_id=review.books_id))
