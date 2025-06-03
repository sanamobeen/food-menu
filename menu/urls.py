from django.urls import path
from menu import views
from .views import create_food_list

urlpatterns = [
    path("menu/fooditem/", create_food_list.as_view(), name="create_food_item"),
   
]