from django import forms
from .models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'variant', 'qty', 'price', 'description']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'variant', 'qty', 'price', 'description']
