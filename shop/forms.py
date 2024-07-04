from django import forms
import re
from .models import *
from django.core.exceptions import ValidationError

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'photo',
            'is_exists',
            'parametr',
            'category',
            'tag'
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_exists': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'parametr': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    parametr = forms.ModelMultipleChoiceField(
        queryset=Parametr.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )


class ProductFilterForm(forms.Form):
    name = forms.CharField(
        label='Название товара',
        required=False,
        min_length=2,
        max_length=150,
        strip=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    min_price = forms.DecimalField(
        label='Минимальная цена',
        required=False,
        min_value=0,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )
    )
    max_price = forms.DecimalField(
        label='Максимальная цена',
        required=False,
        min_value=1,
        decimal_places=2,
        max_digits=10,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        )

   )