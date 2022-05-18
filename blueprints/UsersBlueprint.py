from flask import Blueprint, render_template

from models.User import User
from flask_login import login_required

users = Blueprint('users', __name__)
page_title = 'Users'


@users.route('/')
@login_required
def index():
    all_users = User.query.all()
    return render_template('users/index.html',
                           page_title=page_title,
                           users=all_users)
