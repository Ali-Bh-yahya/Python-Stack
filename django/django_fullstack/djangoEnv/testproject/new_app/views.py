from django.shortcuts import render ,HttpResponse, redirect

# Create your views here.

# def show_template(request):
#   obj ={
#     'name' : "ali",
#     'age' :'21' ,
#     'emails' :['email_1','email_2','email_3']
#   }

#   return render(request,'index.html',obj)

# def some_fun(request):
#   if request.method == "GET":
#     print ('a GET request is being made to this route')
#     return render(request,'some_fun.html')
#   if request.method == "POST":
#     print ('a POST request is being made to this route')
#     return redirect('/')
def index(request):
  return render(request,'home.html')

def user(request):
  print ("Got a Post Info ..................")
  # print (request.POST)
  return render (request,'index.html')

def user_info(request):
  