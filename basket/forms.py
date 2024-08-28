from django import forms

from shop.models import Order

class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, label='Количество', widget=forms.NumberInput(attrs={'class':'form-control'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
        model = Order
        fields = (
            'buyer_name',
            'buyer_firstname',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type'
        )