from app import app
from errors import HttpError
from flask import request, redirect, abort, url_for
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# @app.route('/')
# def home():
#     return redirect(url_for('login'))


@app.route('/login', methods=['GEt', 'POST'])
def login():
    # abort(401)
    # page_not_found(404)
    # error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password)']
        return 'Fine'
    else:
        # error = 'Invalid username/password'
        return render_template('login.html')


@app.route('/user')
def user():
    return 'This page user'


@app.route('/adverts', methods=['GET', 'POST'])
def adverts():
    if request.method != 'GET':
        return 'error'
    else:
        return render_template('base.html')


@app.route('/adverts/<int:adv_id>')
def get_adverts():
    return 'This page for adverts user'
