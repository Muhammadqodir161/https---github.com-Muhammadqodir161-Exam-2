from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_create, name='question_create'),
    path('question_list/',views.question_list,name='question_list'),
]