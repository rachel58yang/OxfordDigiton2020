from django.shortcuts import render
from .models import Post
from random import random


def home(request):
    return render(request, 'letters/index.html', {})

def login(request):
    return render(request, 'letters/login.html', {})

def add_letter(request):
    return render(request, 'letters/add_letter.html', {})

def view_letters(request):
    number_of_records = Post.objects.count()
    random_index = int(random()*number_of_records)+1
    random_letter = Post.objects.get(pk = random_index)
    return render(request, 'letters/view_letters.html', {'letter': random_letter})

def response(request):
    return render(request, 'letters/response.html', {})

