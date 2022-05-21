from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from models.database import db
from utils.mail import mail
from flask_mail import Message
from utils.randomPassword import random_password


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/new_password/<int:user_id>')
def new_password(user_id):
    return render_template('auth/new_password.html', user_id=user_id)


@auth.route('/new_password', methods=['POST'])
def new_password_post():
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('auth.new_password'))
    user = User.query.filter_by(id=user_id).first()
    user.username = user.username
    user.email = user.email
    user.password = generate_password_hash(password, method='sha256')
    user.reset_password = 0
    db.session.commit()
    flash('Password reset successfully,login Now!', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()
    if user.reset_password == 1:
        flash('Please enter new password', 'info')
        return redirect(url_for('auth.new_password', user_id=user.id))
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

    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('auth.register'))
    # check if user already exists in database by email or username
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists', 'danger')
        return redirect(url_for('auth.login'))

    new_user = User(email=email, username=username,
                    password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    flash('You are now registered and can log in', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/reset_password')
def reset_password():
    return render_template('auth/reset_password.html')


@auth.route('/reset_password', methods=['POST'])
def reset_password_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('User email does not exist', 'danger')
        return redirect(url_for('auth.reset_password'))
    token = random_password()
    user.reset_password = 1
    user.password = generate_password_hash(token, method='sha256')
    db.session.commit()

    msg = Message('Password Reset Request',
                  sender='info@bibliophiles.com',
                  recipients=[user.email])
    msg.body = f'To reset your password, Use this temporary token: {token}'
    mail.send(msg)
    flash('An email has been sent with instructions to reset your password', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
