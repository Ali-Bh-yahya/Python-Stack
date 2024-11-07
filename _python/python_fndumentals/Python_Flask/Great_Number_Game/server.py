from flask import Flask ,request , redirect,session , render_template
from random import randint

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
  if "num_rand" not in session:
    session["num_rand"] = randint(1,100)
  print(session["num_rand"])
  return render_template("index.html", num_rand = session["num_rand"])

@app.route("/guess", methods = ["POST"])
def compare_function():
  gusses_num = int(request.form['guess'])
  num_rand = session['num_rand']
  if gusses_num == num_rand:
    session['massage'] = f'{gusses_num} was the number'
    session['won'] = f'{gusses_num} was the number'
    session['color'] = "green"
  elif gusses_num > num_rand:
    session["massage"] = "is too hight!"
    session['color'] = "red"
  else:
    session['massage'] = "is too low!"
    session['color'] = 'red'
  
  return redirect('/')

@app.route('/reset',methods =['POST'])
def reset_game():
  session.clear()
  return redirect('/')


  
if __name__ == "__main__":
  app.run(debug=True)
