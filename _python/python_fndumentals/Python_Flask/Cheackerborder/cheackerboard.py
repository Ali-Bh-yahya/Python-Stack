from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def indexs():
  return render_template('index.html',x=8,y=8)
@app.route('/Y')
def index_Y():
  return render_template('index.html',y=4,x=8)
@app.route('/<int:y>')
def index2(y):
  return render_template('index.html',y=y,x=8)
@app.route('/<int:x>/<int:y>')
def index3(y,x):
  return render_template('index.html',y=y,x=x)
@app.route('/<int:x>/<int:y>/<color>/<color2>')
def checkerborder(x=8,y=8, color=None,color2=None ):
  return render_template('index.html',x=x,y=y,color=color,color2=color2)

if __name__ == '__main__':
  app.run(debug = True)