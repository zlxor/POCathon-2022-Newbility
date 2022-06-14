from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs', views.job, name='jobs'),
    path('match', views.match, name='match'),
    path('post', views.post, name='post'),
    path('login', views.login, name='login'),
    path('signupuser', views.userpage, name='signupuser'),
    path('signupcompany', views.companypage, name='signupcompany'),
    path('register', views.option, name='option'),
]