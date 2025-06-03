from django.contrib import admin
from django.contrib import admin,messages
from .models import FoodItem
class FoodItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price', 'created_by') 
admin.site.register(FoodItem, FoodItemAdmin)

