from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World!'

@app.route('/Champion')
def champion():
  return "Champion!"

@app.route('/say/<name>')
def say_name(name):
  return f"Hi {name}"

@app.route('/repeat/<word>/<id>')

def repeat(id,word):
  return f"{word}  {id}"

if __name__ == '__main__':
  app.run(debug=True)
