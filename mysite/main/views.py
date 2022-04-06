from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    return render(response, 'main/create.html', {})
def view(response):
    return render(response, 'main/view.html', {})
def report(response):
    return render(response, 'main/report.html', {})