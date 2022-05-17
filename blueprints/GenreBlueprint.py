from flask import Blueprint, render_template, request, redirect, jsonify, flash

from models.Genre import Genre
from models.database import db

genres = Blueprint('genres', __name__)

page_title = "Genres"


@genres.route('/')
def index():
    all_genre = Genre.query.all()
    return render_template('genres/index.html',
                           genres=all_genre,
                           page_title=page_title)


@genres.route('show/<int:genre_id>', methods=['GET'])
def show(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return jsonify(genre.serialize())


@genres.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_genre = Genre(name=name, description=description)
        try:
            db.session.add(new_genre)
            db.session.commit()
            flash('Genre successfully added!', 'success')
            return redirect('/genres')
        except:
            flash('There was an issue adding your genre', 'danger')
            return 'There was an issue adding your genre'
    else:
        return "You are not allowed to access this page"


@genres.route('/edit', methods=['GET', 'POST'])
def edit():
    genre_id = request.form['id']
    genre = Genre.query.get_or_404(genre_id)
    if request.method == 'POST':
        genre.name = request.form['name']
        genre.description = request.form['description']
        try:
            db.session.commit()
            flash('Genre successfully edited!', 'success')
            return redirect('/genres')
        except:
            flash('There was an issue editing your genre', 'danger')
            return 'There was an issue editing your genre'
    else:
        return "You are not allowed to access this page"


@genres.route('/delete/<int:genre_id>', methods=['POST', 'GET'])
def delete(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    try:
        db.session.delete(genre)
        db.session.commit()
        flash('Genre successfully deleted!', 'success')
        return redirect('/genres')
    except:
        flash('There was an issue deleting your genre', 'danger')
        return 'There was an issue deleting your genre'
