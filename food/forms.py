from django import forms
from food.models import Food,Customer

class Foodform(forms.ModelForm):
    class Meta:
        model=Food
        fields='__all__'

class Customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'