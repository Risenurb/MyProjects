from django.urls import path
from . import views

urlpatterns = [
    path('foodapi', views.foodList, name='api1'),
    path('foodapi/<int:id>', views.fooditem, name='foodapi'),
    path('food/suggestion', views.result, name='result'),
    path('addfood/', views.addFood, name ='addfood' ),
    path('', views.menu, name='menu'),
    ]