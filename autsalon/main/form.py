from django import forms
from .models import Brand, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country', 'founded_at']
        widgets = {
            'founded_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'photo', 'model_year', 'price', 'brand']
