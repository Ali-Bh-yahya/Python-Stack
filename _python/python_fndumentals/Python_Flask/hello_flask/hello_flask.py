from flask import Flask , render_template # Import Flask to allow us to create our app

app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route('/s')
def success():
  return 'Success'

@app.route('/hello/<name>')
def hello_person(name):
  return f'Hello, {name}!'

@app.route('/user/<username>/<id>')
def user_user(username,id):
  return f"user name = {username}     user ID = {id} "

@app.route('/ht')
def user_ht():
  return render_template('index.html', phrase="hello",times=5 )
if __name__ == '__main__':
  app.run(debug=True)






