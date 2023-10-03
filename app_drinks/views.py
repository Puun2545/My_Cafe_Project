from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

all_drinks = [
    {
        'id' : 1, 'title' : 'Dark Choco Frappe', 'price' : 1100, 'is_premium' : False,
        'promotion_end' : datetime(2023, 12 , 12)
    },
    {
        'id' : 2, 'title' : 'Oat Milk Macha', 'price' : 1120, 'is_premium' : True,
        'promotion_end' : datetime(2023, 12 , 12)
    },
    {
        'id' : 3, 'title' : 'Pan Thai Milk Tea', 'price' : 1120, 'is_premium' : True,
        'promotion_end' : datetime(2023, 12 , 12)
    },
    {
        'id' : 4, 'title' : 'Pun Choco Latte', 'price' : 1110, 'is_premium' : True,
        'promotion_end' : None
    },
    {
        'id' : 5, 'title' : 'Guy Mix Berry', 'price' : 1110, 'is_premium' : True,
        'promotion_end' : None
    }
]

def drinks(request):
    context = { 'drinks' : all_drinks }
    return render(request, 'app_drinks/drinks.html', context)

def drink_info(request, drink_id):
    one_drink = None
    try:
        one_drink = [f for f in all_drinks if f['id'] == drink_id][0]
    except:
        print('ไม่มีเธอ ไม่มีเธอ')
    context = { 'drink' : one_drink}
    return render(request, 'app_drinks/drink_info.html', context)
