from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def include_your_ifo():
  return render_template('index.html')

@app.route('/result',methods=['POST'])
def print_result():
  name = request.form['name']
  location = request.form['location']
  language = request.form['language']
  comment = request.form['comment']
  # print(f"Name: {name}, Location: {location}, Language: {language}")
  return render_template('result.html',name=name , location=location , language=language , comment=comment)

if __name__ == '__main__':
  app.run(debug=True)