from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
# from menu.utils import get_expired_food_item, return_response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodItemSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from menu.models import FoodItem
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class create_food_list(ListAPIView):
  permission_classes = [IsAuthenticated]
  
  def get(self,request):
    
    food_items =FoodItem.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 5  # Set your desired page size

    result_page = paginator.paginate_queryset(food_items, request)
    serializer = FoodItemSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)