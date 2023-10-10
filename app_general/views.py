from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from app_drinks.models import Drink
from .forms import Subscription_form
from .models import Subscription

# Create your views here.
def home(request):
    return render(request, 'app_general/myfirst.html')

def about(request):
    return render(request, 'app_general/about.html')

def subs(request):
    if request.method == 'POST':
        form = Subscription_form(request.POST)
        if form.is_valid() :
            data = form.cleaned_data
            new_subs = Subscription()
            new_subs.name = data['name']
            new_subs.email = data['email']
            print(data)
            new_subs.save()
            new_subs.drink_set.set(data['drinks_set'])
        return HttpResponseRedirect('thanks')
        
    form = Subscription_form()
    context = {'form': form}
    return render(request, 'app_general/subs_form.html', context)

def thanks(request):
    return render(request, 'app_general/thanks.html')



