from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from models.database import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
  # login code goes here
    pass

@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/register', methods=['POST'])
def register_post():

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    usertype_id = 1

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.login'))

    new_user = User(email=email, username=username, usertype_id=usertype_id,
                    password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

    # @auth.route('/logout')
    # @login_required
