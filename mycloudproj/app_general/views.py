from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'app_general/myfirst.html')

def about(request):
    return render(request, 'app_general/about.html')
