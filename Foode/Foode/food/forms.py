from django import forms  
from food.models import Food
from django.forms import fields

class FoodForm(forms.ModelForm):  
    class Meta:  
        model = Food  
        fields = "__all__"  