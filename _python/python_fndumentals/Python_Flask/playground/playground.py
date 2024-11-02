from flask import Flask , render_template
##https://github.com/Ali-Bh-yahya/Python-Stack/tree/master/_python/python_fndumentals/Python_Flask/playground##
##Here is the link to my assignment in my GitHub repository##
app = Flask(__name__)

@app.route('/play')
def play():
  return render_template('play.html',x=3, backgroun_color= "blue")

@app.route('/play/<int:x>')

def play_x(x):
  return render_template('play.html',x=x,backgroun_color =  'blue')
@app.route('/play/<int:x>/<backgroun_color>')

def play_x_color(x,backgroun_color):
  return render_template('play.html',x=x,backgroun_color=backgroun_color)

if __name__ == '__main__':
  app.run(debug=True)