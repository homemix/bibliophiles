from flask import Blueprint, render_template, redirect, url_for, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register')
def register():
    return render_template('auth/register.html')
