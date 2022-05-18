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
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.', 'danger')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    flash('You have successfully logged in', 'success')
    return redirect(url_for('books.index'))


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    usertype_id = 1
    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('auth.register'))
    # check if user already exists in database by email or username
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists', 'danger')
        return redirect(url_for('auth.login'))

    new_user = User(email=email, username=username, usertype_id=usertype_id,
                    password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    flash('You are now registered and can log in', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
