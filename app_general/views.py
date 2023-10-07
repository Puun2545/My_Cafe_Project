from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from app_drinks.models import Drink

# Create your views here.
def home(request):
    return render(request, 'app_general/myfirst.html')

def about(request):
    return render(request, 'app_general/about.html')

def subs(request):
    all_drinks = Drink.objects.order_by('-is_premium')
    context = {'drinks': all_drinks}
    return render(request, 'app_general/subs_form.html', context)

def thanks(request):
    return render(request, 'app_general/thanks.html')



