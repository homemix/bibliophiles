from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify

from models.User import User
from models.UserType import UserType
from flask_login import login_required
from models.database import db

users = Blueprint('users', __name__)
page_title = 'Users'


@users.route('/')
@login_required
def index():
    all_users = User.query.all()
    user_types = UserType.query.all()
    return render_template('users/index.html',
                           page_title=page_title,
                           user_types=user_types,
                           users=all_users)


@users.route('/show/<int:user_id>')
@login_required
def show(user_id):
    user = User.query.get_or_404(user_id)
    if user:
        return jsonify(user.serialize())


@users.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    user_id = request.form.get('user_id')
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.usertype_id = request.form.get('usertype_id')
        try:
            db.session.commit()
            flash('User updated successfully', 'success')
            return redirect(url_for('users.index'))
        except:
            flash('Error updating user', 'danger')
            return redirect(url_for('users.index'))
    else:
        flash('Error updating user', 'danger')
        return redirect(url_for('users.index'))
