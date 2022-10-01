from rest_framework import  serializers
from .models import FoodSuggestion
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodSuggestion
        fields = ["id", "ingr1", "ingr2", "ingr3"]