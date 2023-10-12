from django.contrib import admin
from .models import Drink

# Register your models here.

class DrinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'promotion_price', 'is_premium', 'promotion_end_at']
    search_fields = ['title']
    list_filter = ['is_premium']

admin.site.register(Drink, DrinkAdmin)