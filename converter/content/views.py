# views.py

from django.shortcuts import render

def home(request):
    return render(request, 'content/home.html')