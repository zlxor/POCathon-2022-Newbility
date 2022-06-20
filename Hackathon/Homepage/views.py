from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserSignupForm, CompanySignupForm, PostJobs

import requests
  
#Affindi Endpoint
API_ENDPOINT = "https://cloud-wallet-api.prod.affinity-project.org/api/v1/users/signup"
  
#API key
API_KEY = "4edb317b-d442-4f66-b848-baa9e6f8df7a"

  
# sending post request and saving response as response object
#r = requests.post(url = API_ENDPOINT, data = data)

def index(request):
    return render(request, 'index.html')

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def signup(request):
    return render(request, 'signup.html')

def signupuser(request):
    form = UserSignupForm()
    return render(request, 'individual_signup.html', {'form' : form})

def signupcompany(request):
    form = CompanySignupForm()
    return render(request, 'company_signup.html', {'form' : form})

def user(request):
    return render(request, 'user.html')

def company(request):
    form = PostJobs()
    return render(request, 'company.html', {'form' : form})

def jobinfo(request):
    return render(request, 'job_display.html')

def recommend(request):
    return render(request, 'recommend.html')
#def registeruser(request):
#    msg = None
#    if(request.method == 'POST'):
#        form = SignupForm(request.POST)
#        if(form.is_valid()):
#            form.save()
##            print(Data.is_user)
##            Data.is_user = 1
##            print(Data.is_user)
##            print(Data.save())
#            msg = 'Account Created'
#            return HttpResponseRedirect('signupuser')
#        else:
#            msg = form.errors
#            print(msg)
#    else:
#        form = SignupForm()
#    return render(request, 'signupuser.html', {'form' : form, 'msg': msg})
#
#def registercompany(request):
#    msg = None
#    if(request.method == 'POST'):
#        form = SignupForm(request.POST)
#        if(form.is_valid()):
#            form.is_company = True
#            form.save()
#            msg = 'Account Created'
#            return redirect('login')
#        else:
#            msg = 'Form is not valid'
#    else:
#        form = SignupForm()
#    return render(request, 'signupcompany.html', {'form' : form, 'msg': msg})
#
#
#def login(request):
#    msg = None
#    if(request.method == 'POST'):
#        form = LoginForm()
#        if(form.is_valid()):
#            Username = form.cleaned_data.get('username')
#            Password = form.cleaned_data.get('password')
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                login(request, user)
#                return redirect('home')
#            else:
#                msg = 'Invalid Email/Password'
#            return redirect('index')
#        else:
#            msg = 'Error validating form'
#    else:
#        form = LoginForm()
#    return render(request, 'login.html', {'form' : form, 'msg': msg})
#
#
#def job(request):
#    return render(request, 'jobs.html')
#
#def matchTalents(request):
#    return render(request, 'matchTalents.html')
#
#def post(request):
#    return render(request, 'post.html')
#
#
#def login(request):
#    return render(request, 'login.html')
#
#def userpage(request):
#
#    return render(request, "signupuser.html")
#
#
#def companypage(request):
#
#    return render(request, "companypage.html")
#
#
#def option(request):
#    return render(request, 'option.html')
#
#
#def rec(request):
#    return render(request, 'recommend.html')

