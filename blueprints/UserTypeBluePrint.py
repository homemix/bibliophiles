from flask import Blueprint, render_template, request, redirect, jsonify, flash

from models.UserType import UserType
from models.database import db

userTypes = Blueprint('userTypes', __name__)
page_title = 'User Types'


@userTypes.route('/')
def index():
    all_user_types = UserType.query.all()
    return render_template('userTypes/index.html',
                           userTypes=all_user_types,
                           page_title=page_title)


@userTypes.route('show/<int:user_type_id>', methods=['GET'])
def show(user_type_id):
    user_type = UserType.query.get_or_404(user_type_id)
    return jsonify(user_type.serialize())


@userTypes.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_user_type = UserType(name=name, description=description)
        try:
            db.session.add(new_user_type)
            db.session.commit()
            flash('User Type Created Successfully', 'success')
            return redirect('/userTypes')
        except:
            flash('There was an issue creating your user type', 'danger')
            return 'There was an issue adding your user type'
    else:
        return "You are not allowed to access this page"


@userTypes.route('/edit', methods=['GET', 'POST'])
def edit():
    user_type_id = request.form['id']
    user_type = UserType.query.get_or_404(user_type_id)
    if request.method == 'POST':
        user_type.name = request.form['name']
        user_type.description = request.form['description']
        try:
            db.session.commit()
            flash('User Type Updated Successfully', 'success')
            return redirect('/userTypes')
        except:
            flash('There was an issue updating your user type', 'danger')
            return 'There was an issue editing your user type'
    else:
        return "You are not allowed to access this page"


@userTypes.route('/delete/<int:user_type_id>', methods=['POST', 'GET'])
def delete(user_type_id):
    user_type = UserType.query.get_or_404(user_type_id)
    try:
        db.session.delete(user_type)
        db.session.commit()
        flash('User Type Deleted Successfully', 'success')
        return redirect('/userTypes')
    except:
        flash('There was an issue deleting your user type', 'danger')
        return 'There was an issue deleting your user type'
