from django import forms
from django.db.models.base import Model
from app_drinks.models import Drink
from .models import Subscription

class DrinkMultipleChoiceField(forms.ModelMultipleChoiceField) :
    def label_from_instance(self, obj) :
        return obj.title

class Subscription_form(forms.Form) :
    name = forms.CharField(max_length=60, required=True, label='ชื่อ - นามสกุล')
    email = forms.EmailField(max_length=60, required=True, label='email')
    drinks_set = DrinkMultipleChoiceField(
        queryset=Drink.objects.order_by('-is_premium'), 
        required=True, 
        label='เลือกเมนู',
        widget=forms.CheckboxSelectMultiple
    )
    accept = forms.BooleanField(required=True, label='ยอมรับขอตกลง')
    
class SubscriptionModelForm(forms.ModelForm):
    
    drinks_set = DrinkMultipleChoiceField(
        queryset=Drink.objects.order_by('-is_premium'), 
        required=True, 
        label='เลือกเมนู',
        widget=forms.CheckboxSelectMultiple
    )
    
    accepted = forms.BooleanField(required=True, label='ยอมรับขอตกลง')
    
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'drinks_set', 'accepted']
        labels = {
            'name' : 'ชื่อ - นามสกุล',
            'email' : 'อีเมล',
            'drinks_set' : 'เมนูที่สนใจ',
        }
