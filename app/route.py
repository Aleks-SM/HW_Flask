from app import app
from flask import request, redirect, abort, url_for
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    # abort(401)
    page_not_found()


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
