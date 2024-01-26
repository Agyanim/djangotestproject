from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Student,Users
from .controller import aboutController
from django.contrib.auth.models import User
from django.contrib import auth,messages


# Create your views here.
# home end point
def index (request):
  
   return render(request,"index.html")

# about endpoint
def aboutpage(req):
    return aboutController()

def counter(request):
    words=request.POST["words"]
    count_words=len(words.split())
    return render(request,"counter.html",{"words":count_words})

def about(request):
    studentList=Student.objects.all()
    return render(request,"about/about.html",{"studentList":studentList})

def signup(request):
    return render(request,"signup.html")


def login(request):
    username=request.POST['username']
    password=request.POST['password']
    print(username)
    if (len(username) ==0):
        messages.info(request,'username field cannot be empty')
    elif (len(password) ==0):
        messages.info(request,'password field cannot be empy')
    else:
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'no user found')
    return render(request,'signin.html')



def register(request):
    username=request.POST['username']
    password=request.POST["password"]
    
    if User.objects.filter(username=username).exists():
        messages.info(request,"User already exist!")
        return redirect('signup')
        
    else:
        user=User.objects.create_user(username=username,password=password)
        user.save()
    return redirect('signin')

def signin(request):
   return render(request,'signin.html')

