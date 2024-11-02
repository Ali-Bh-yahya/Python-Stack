from flask import Flask , render_template , request , redirect , session

app = Flask(__name__)

app.secret_key = 'secret_key'

@app.route('/')
def counter():
    if 'counter' not in session:
        session['counter'] = 0  
    session['counter'] += 1 
    return render_template('index.html', counte=session['counter'])
  
@app.route('/destroy_session')
def destroy_session():
   session.clear()
   return redirect('/')

@app.route('/handle_action', methods=['POST'])
def add2():
    if request.form['btn'] == 'add2':
        session['counter'] += 2
    elif request.form['btn'] == 'reset':
        session.pop('counter')
    return redirect("/")

if __name__ == '__main__':
  app.run(debug=True)