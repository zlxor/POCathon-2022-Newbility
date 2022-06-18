from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.option, name='option'),
    path('signupuser', views.registeruser, name='signupuser'),
    path('signupcompany', views.registercompany, name='signupcompany'),
    path('jobs', views.job, name='jobs'),
    path('match', views.match, name='match'),
    path('post', views.post, name='post'),
    path('login', views.login, name='login'),
    path('rec', views.rec, name='rec'),

]