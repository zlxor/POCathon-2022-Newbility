from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render(request, 'index.html')
#Matching
#Scam
#Affindi API
def registeruser(request):
    msg = None
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.save()
#            print(Data.is_user)
#            Data.is_user = 1
#            print(Data.is_user)
#            print(Data.save())
            msg = 'Account Created'
            return HttpResponseRedirect('signupuser')
        else:
            msg = form.errors
            print(msg)
    else:
        form = SignupForm()
    return render(request, 'signupuser.html', {'form' : form, 'msg': msg})

def registercompany(request):
    msg = None
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        if(form.is_valid()):
            form.is_company = True
            form.save()
            msg = 'Account Created'
            return redirect('login')
        else:
            msg = 'Form is not valid'
    else:
        form = SignupForm()
    return render(request, 'signupcompany.html', {'form' : form, 'msg': msg})


def login(request):
    msg = None
    if(request.method == 'POST'):
        form = LoginForm()
        if(form.is_valid()):
            Username = form.cleaned_data.get('username')
            Password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Invalid Email/Password'
            return redirect('index')
        else:
            msg = 'Error validating form'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form' : form, 'msg': msg})


def job(request):
    return render(request, 'jobs.html')

def match(request):
    return render(request, 'match.html')

def post(request):
    return render(request, 'post.html')


def login(request):
    return render(request, 'login.html')

def userpage(request):

    return render(request, "signupuser.html")


def companypage(request):

    return render(request, "signupcompany.html")


def option(request):
    return render(request, 'option.html')


def rec(request):
    return render(request, 'recommend.html')

