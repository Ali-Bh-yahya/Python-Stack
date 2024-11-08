from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)  # Print the form data for debugging
    strawberry = request.form['strawberry']
    apple = request.form['apple']
    raspberry = request.form['raspberry']
    first_name =request.form['first_name']
    last_name = request.form['last_name']
    Student_Id =request.form['student_id']
    total = int(strawberry)+ int(raspberry) + int(apple)
    time = datetime.now()
    date_time = time.strftime("%m/%d/%Y,%H:%M:%S")
    return render_template("checkout.html",strawberry=strawberry,apple=apple,raspberry=raspberry,first_name=first_name,last_name=last_name,Student_Id=Student_Id,total=total
    ,time=time,the_date = date_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    