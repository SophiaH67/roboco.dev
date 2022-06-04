from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'roboco/index.html')

def why(request):
    return render(request, 'roboco/why.html')