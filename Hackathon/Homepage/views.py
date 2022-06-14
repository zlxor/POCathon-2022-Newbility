from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def job(request):
    return render(request, 'jobs.html')

def match(request):
    return render(request, 'match.html')

def post(request):
    return render(request, 'post.html')


def login(request):
    return render(request, 'login.html')

def userpage(request):
    return render(request, 'user.html')

def companypage(request):
    return render(request, 'company.html')

def option(request):
    return render(request, 'option.html')

