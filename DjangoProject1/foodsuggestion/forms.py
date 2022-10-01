from django.forms import ModelForm
from .models import FoodSuggestion


class FoodsuggestionForm(ModelForm):
    class Meta:
        model = FoodSuggestion
        fields = ["Dish_Name","ingredient2","ingredient3","ingredient4","img"]

