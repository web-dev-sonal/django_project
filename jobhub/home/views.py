from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def home_page(request):
    res = render(request,'home/Home.html')
    return res

def about(request):
    res = render(request,'home/about.html')
    return res

def contact(request):
    res = render(request,'home/contact.html')
    return res

def Login(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            s="loggedin successfully! <br> <a href='/home'>Go To HomePage</a>"
            return HttpResponse(s)
        else:
            data['error']="Username or Password is incorrect"
            res = render(request,'home/Login.html',data)
            return res
    else:
        return render(request,'home/Login.html',data)
