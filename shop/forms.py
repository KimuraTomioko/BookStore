from django import forms
from .models import *

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'create_date',
            'update_date',
            'photo',
            'is_exists',
            'parametr',
            'category',
            'tag'
        )

        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.FloatField(attrs={'class':'form-control'}),
            'create_date': forms.DateTimeField(attrs={'class': 'form-control'}),
            'update_date': forms.DateTimeField(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_exists': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'parametr': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class':'form-control'})
        }
    

    parametr = forms.ModelMultipleChoiceField(
        queryset=Parametr.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'})
    )

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
