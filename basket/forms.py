from django import forms

class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, label='Количество', widget=forms.NumberInput(attrs={'class':'form-control'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)