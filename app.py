from flask import Flask, render_template
from dotenv import load_dotenv
import os
from models.database import db
from models import Books, Genres, Reviews, Users, UserTypes

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/books')
def view_books():
    page_title = 'Books'
    return render_template('books/index.html', page_title=page_title)


if __name__ == '__main__':
    app.run()
