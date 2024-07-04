from django.shortcuts import redirect, render
from .models import *
from .forms import * 
from django.contrib.auth.decorators import login_required, permission_required

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

    return render(request, 'shop/product/filter.html', context)


def get_more_filter_product(request):
    find_product = Product.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/query_filter_product.html', context)


def product_catalog_with_filter(request):
    list_product = Product.objects.all()
    if request.GET:
        product_form = ProductFilterForm(request.GET)
    else:
        product_form = ProductFilterForm()

    if product_form.is_valid():
        if product_form.cleaned_data.get('name'):
            list_product = list_product.filter(name__icontains=product_form.cleaned_data.get('name'))
        if product_form.cleaned_data.get('min_price'):
            list_product = list_product.filter(price__gte=product_form.cleaned_data.get('min_price'))
        if product_form.cleaned_data.get('max_price'):
            list_product = list_product.filter(price__lte=product_form.cleaned_data.get('max_price'))
        
    context = {
        'product_list': list_product,
        'form': product_form
    }
    return render(request, 'shop/product/catalog_with_filter.html', context)



@login_required
def create_product(request):
    if request.method == 'POST':
        product_create_form = ProductCreationForm(request.POST)
        if product_create_form.is_valid():
            product_create_form.save()
            return redirect('product_list')
        else:
            return render(request, 'shop/product/create_product.html', {'form': product_create_form})
    else:
        product_create_form = ProductCreationForm()
        return render(request, 'shop/product/create_product.html', {'form': product_create_form})



    

    