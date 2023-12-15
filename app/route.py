
@app.route('/')
def home():
  return 'This is main page'


@app.route('/user')
def user():
  return 'This page user'


@app.route('/adverts')
def adverts():
  return 'This page for adverts user'
