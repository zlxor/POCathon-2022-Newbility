from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs', views.job, name='jobs'),
    path('match', views.match, name='match'),
    path('post', views.post, name='post'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]