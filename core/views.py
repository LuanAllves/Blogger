from django.shortcuts import render
from django.http import request

# Create your views here.
def HomeView(request):
    return render(request, 'core/home.html')
