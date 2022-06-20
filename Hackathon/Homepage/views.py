from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm, UserSignupForm, CompanySignupForm, PostJobs
from django.views.decorators.csrf import csrf_exempt  
from .models import Individual, Company  
import requests
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


#Affindi Endpoint
SIGNUP = "https://cloud-wallet-api.prod.affinity-project.org/api/v1/users/signup"
LOGIN = 'https://cloud-wallet-api.prod.affinity-project.org/api/v1/users/login'
#API key
API_KEY = {'Api-Key' :"ede388293715a2b2da022caea7819beb5a61eb72e3b58d92b472112663b86055"}

  
# sending post request and saving response as response object
#r = requests.post(url = API_ENDPOINT, data = data)

def index(request):
    return render(request, 'index.html')


def login(request):
    msg = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if(form.is_valid()):
            

            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = LOGIN, params = Payload, headers = API_KEY)
            #print(r)

            if(form.cleaned_data['Choice'] == '1'):
                for Data in Individual.objects.all():
                    if(Data.Email == form.cleaned_data['Email']):
                        if(Data.Password == form.cleaned_data['Password']):
                            return HttpResponseRedirect('company')
                msg = 'Wrong Email/Password'
                
            else:
                for Data in Individual.objects.all():
                    if(Data.Email == form.cleaned_data['Email']):
                        if(Data.Password == form.cleaned_data['Password']):
                            return HttpResponseRedirect('user')
                msg = 'Wrong Email/Password'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form, 'msg' : msg})

def signupuser(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if(form.is_valid()):
            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = SIGNUP, params = Payload, headers = API_KEY)
            #print(r)
            form.save()
            return HttpResponseRedirect('login')
        else:
            print(form.errors)
    else:
        form = UserSignupForm()
        
    return render(request, 'individual_signup.html', {'form' : form})

def signupcompany(request):
    if request.method == 'POST':
        form = CompanySignupForm(request.POST)
        if(form.is_valid()):
            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = SIGNUP, params = Payload, headers = API_KEY)
            #print(r)
            form.save()
            return HttpResponseRedirect('login')
        else:
            print(form.errors)
    else:
        form = CompanySignupForm()
    return render(request, 'company_signup.html', {'form' : form})


def company(request):
    if request.method == 'POST':
        form = PostJobs(request.POST)
        if(form.is_valid()):
            #Payload = {
            #    "username": form.cleaned_data['Email'],
            #    "password": form.cleaned_data['Password']
            #}
            #r = requests.post(url = SIGNUP, params = Payload, headers = API_KEY)
            #print(r)
            form.save()
    else:
        form = PostJobs()
    return render(request, 'company.html', {'form' : form})

def user(request):
    return render(request, 'user.html')

def signup(request):
    return render(request, 'signup.html')

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

