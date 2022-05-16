from flask import Flask, render_template
from dotenv import load_dotenv
import os
from models.database import db
from models.Book import Book
from models.Genre import Genre
from models.User import User
from models.Review import Review
from models.UserType import UserType

from blueprints.BooksBlueprint import books
from blueprints.GenreBlueprint import genres
from blueprints.UserTypeBluePrint import userTypes
from blueprints.ReviewBluprint import reviews

app = Flask(__name__)
app.url_map.strict_slashes = False

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_SERVER = os.getenv('DB_SERVER')
app.config['SECRET_KEY'] = os.getenv("MY_SECRET")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)


app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(genres, url_prefix='/genres')
app.register_blueprint(userTypes, url_prefix='/userTypes')
app.register_blueprint(reviews, url_prefix='/reviews')


@app.route('/')
def index():
    page_title = 'Books'
    return render_template('base.html', page_title=page_title)


if __name__ == '__main__':
    app.run()
