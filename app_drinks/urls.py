from django.urls import path
from . import views

urlpatterns = [
    path('', views.drinks, name="drinks"),
    path('<int:drink_id>', views.drink_info, name="drink_info")
]