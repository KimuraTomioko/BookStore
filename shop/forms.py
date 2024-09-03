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
            'parametr',
            'category',
            'tag'
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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

class FeebBack(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

        widgets = {
            'rating': forms.NumberInput(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class':'form-control'})
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'agent_lastname', 'agent_name', 'agent_surname', 'agent_telephone', 'address', 'is_exists')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'agent_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'agent_name': forms.TextInput(attrs={'class':'form-control'}),
            'agent_surname': forms.TextInput(attrs={'class':'form-control'}),
            'agent_telephone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'is_exists':forms.CheckboxInput(attrs={'class':'form-control'})
        }

class AddWarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ('location','capacity')

        widgets = {
            'location': forms.TextInput(attrs={'class':'form-contol'}),
            'capacity': forms.NumberInput(attrs={'class':'form-control'})
        }

class AddOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('buyer_lastname', 'buyer_name', 'buyer_surname', 'comment', 'delivery_address', 'delivery_type', 'date_finish', 'product')

        widgets = {
            'buyer_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'buyer_surname': forms.TextInput(attrs={'class':'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-contorl'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-contorl'}),
            'delivery_type': forms.Select(attrs={'class': 'form-contorl'}),
            'date_finish': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'product': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
    
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.SelectMultiple(attrs={'class':'form-control'}),
        required = False
    )

''' class Return(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    reason = models.TextField(verbose_name='Причина возврата')
    date_returned = models.DateTimeField(verbose_name='Дата возврата')

    def __str__(self):
        return f'{self.order.pk} - {self.date_returned}'

    class Meta:
        verbose_name = 'Возврат'
        verbose_name_plural = 'Возвраты'
'''

class ReturnProductForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = ('order', 'reason', 'date_returned')

        widgets = {
            'order': forms.Select(),
            'reason': forms.Textarea(attrs={'class':'form-control'}),
            'date_returned': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
