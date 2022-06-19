from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.option, name='option'),
    path('signupuser', views.registeruser, name='signupuser'),
    path('signupcompany', views.registercompany, name='signupcompany'),
    path('companypage', views.companypage, name='companypage'),
    path('jobs', views.job, name='jobs'),
    path('matchTalents', views.matchTalents, name='matchTalents'),
    path('post', views.post, name='post'),
    path('login', views.login, name='login'),
    path('rec', views.rec, name='rec'),

]