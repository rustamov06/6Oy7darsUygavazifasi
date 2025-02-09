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


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'photo', 'model_year', 'price', 'brand']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'model_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
        }
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country', 'founded_at']
        labels = {
            'name': 'Brend nomi',
            'country': 'Kelib chiqishi',
            'founded_at': 'Tashkil topgan vaqti'
        }
        widgets = {
            'founded_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }