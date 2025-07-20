from django.shortcuts import render

# Create your views here.

# testing code start
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world from myapp...")
# testing code end
