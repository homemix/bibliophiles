from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/books')
def view_books():
    page_title = 'Books'
    return render_template('books/index.html', page_title=page_title)


if __name__ == '__main__':
    app.run()
