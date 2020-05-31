from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('addLetter', views.add_letter, name='add_letter'),
    path('addLetter/new', views.post_new, name='post_new'),
    path('letters', views.view_letters, name='view_letters'),
    path('response/<int:id>/', views.response, name='response')
]