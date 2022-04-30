from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http

# Create your views here.

def index(request):
    return HttpResponse('<h1>Welcome home </h1>')
