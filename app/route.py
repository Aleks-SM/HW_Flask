from app import app
from flask import request
from flask import render_template

@app.route('/')
def home():
  return 'This is main page'


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
