from django.shortcuts import render,redirect

# Create your views here.
def root(request):
  return redirect('')
def index(request):

  users= {
    'data': [
    {'first_name': 'Ali','last_name':'Yahya','email':'adsa@gjas','phone':'0593322640'},
    {'first_name': 'Yasser','last_name':'Bds','email':'adsa@gjas','phone':'0593322640'},
    {'first_name': 'Loai','last_name':'zadian','email':'1111@gjas','phone':'0593322640'},#statement must be separated by newlines or 
    {'first_name': 'ZAk','last_name':'Zakaria','email':'adsa@gjas','phone':'0593322640'} 
    ]
    }
  print(users['data'])
   

  return render(request,'index.html',users)

