from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_letter, name='add_letter'),
    path('letters', views.view_letters, name='view_letters'),
    path('response', views.response, name='response')
]