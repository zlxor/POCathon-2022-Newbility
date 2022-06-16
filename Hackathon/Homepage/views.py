from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import UserSignup, CompanySignup
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
    if request.method == "POST":
        form = UserSignup(request.POST)
        if form.is_valid():
            form.HashKey = "TO ENTER"
            form.save()

            return HttpResponseRedirect(reverse('index') )
    form = UserSignup()
    return render(request, "user.html", {"form": form})


def companypage(request):
    if request.method == "POST":
        form = CompanySignup(request.POST)
        if form.is_valid():
            form.HashKey = "TO ENTER"
            form.save()

            return HttpResponseRedirect(reverse('index') )
    form = CompanySignup()
    return render(request, "company.html", {"form": form})


def option(request):
    return render(request, 'option.html')

