from django.db import models


# Create your models here.
class FoodSuggestion(models.Model):
    Dish_Name = models.CharField(max_length=100)
    ingredient2 = models.CharField(max_length=50)
    ingredient3 = models.CharField(max_length=50)
    ingredient4 = models.CharField(max_length=50)
    img = models.ImageField(upload_to="picsfood")
    price_range = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Dish_Name

class Price(models.Model):
    price_range1 = models.CharField(max_length=70)
    price_range1_name =models.CharField(max_length=100)
