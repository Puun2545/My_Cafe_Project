from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Subscription_form, SubscriptionModelForm
from .models import Subscription

# Create your views here.
def home(request):
    return render(request, 'app_general/myfirst.html')

def about(request):
    return render(request, 'app_general/about.html')

def subs(request):
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        form = SubscriptionModelForm()
    context = {'form': form}
    return render(request, 'app_general/subs_form.html', context)

def thanks(request):
    return render(request, 'app_general/thanks.html')



