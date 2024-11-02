
from flask import Flask, render_template
##https://github.com/Ali-Bh-yahya/Python-Stack/tree/master/_python/python_fndumentals/Python_Flask/HTML_TABLE/Ass4_More%20Template%20Rendering ##

##Here is the link to  my assignment in my GitHub repository##
app = Flask(__name__)


@app.route('/')
def Checkerboard():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html",users=users)








if __name__=="__main__":
    app.run(debug=True)