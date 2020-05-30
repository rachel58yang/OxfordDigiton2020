from django.shortcuts import render
from .forms import PostForm


def home(request):
    return render(request, 'letters/index.html', {})

def login(request):
    return render(request, 'letters/login.html', {})

def add_letter(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.response = 0;
            post.save()
            return redirect('letters/add_letter.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'letters/add_letter.html', {})

def view_letters(request):
    return render(request, 'letters/view_letters.html', {})

def response(request):
    return render(request, 'letters/response.html', {})

