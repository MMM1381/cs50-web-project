from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/forms.html")

def MMM(request):
    return HttpResponse("Hello Mehdi")

def laugh (request):
    return HttpResponse("hahahahah")

def greet(request, name):
    return HttpResponse(f"Hello {name}")