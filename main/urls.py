from django.contrib import admin
from django.urls import path
from main import views
from .views import *

app_name = "main"
urlpatterns = [
    path('', views.showmain, name="showmain"),
    path('mentors/', views.showmentors, name="showmentors"),
    path('contact/', views.showcontact, name="showcontact"),
    path('recruit/', views.showrecruit, name="showrecruit"),
    path('dff/', views.showdff, name="showdff"),
    path('announce/', views.showannounce, name="showannounce"),
    path('message/', views.showmessage, name="showmessage"),
    path('dreamer/', views.showdreamer, name="showdreamer"),
    path('toMentor/', views.showtoMentor, name="showtoMentor"),
    path('new/', views.showNew, name="showNew"),
    path('foryou/', views.showForyou, name="showForyou"),
    path('complete/', views.showcomplete, name="showcomplete"),
    path('create/', views.create, name="create"),
    path('delete/<str:id>', views.delete, name="delete"),
]