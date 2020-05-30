from django.shortcuts import render


def home(request):
    return render(request, 'letters/index.html', {})

def add_letter(request):
    return render(request, 'letters/add_letter.html', {})

def view_letters(request):
    return render(request, 'letters/view_letters.html', {})

def response(request):
    return render(request, 'letters/response.html', {})

