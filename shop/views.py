from django.shortcuts import redirect, render
from .models import *
from .forms import * 


def product_list(request):
    list_product = Product.objects.all()
    context = {
        'product_list': list_product
    }
    return render(request, 'shop/product/catalog.html', context)


def get_one_filter_product(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'find_product': find_product
    }

    return render(request, 'shop/product/filter.html')






def create_product(request):
    if request.method == 'POST':
        product_create_form = ProductCreationForm(request.POST)
        if product_create_form.is_valid():
            new_product_create_form = ProductCreationForm(**product_create_form.cleaned_data)
            new_product_create_form.save()
            return redirect('catalog')
        else:
            return render(request, 'shop/product/create_product.html', {'form': product_create_form})
    
    else:
        product_creation_form = ProductCreationForm()
        return render(request, 'shop/product/create_product.html', {'form': product_create_form})
    

    