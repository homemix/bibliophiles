from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.User import User

users = Blueprint('users', __name__)
page_title = 'Users'


@users.route('/', )
def index():
    all_users = User.query.all()
    return render_template('users/index.html',
                           page_title=page_title,
                           users=all_users)
