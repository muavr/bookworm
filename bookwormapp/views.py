from django.shortcuts import render


def home(request):
    return render(request, 'bookwormapp/home.html')


def profile(request):
    return render(request, 'bookwormapp/profile.html')
