from django.db import models
from registration.models import User
from django.conf import settings


class FoodItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    manufacturing_date = models.DateField()
    expiration_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        
        
        return self.name