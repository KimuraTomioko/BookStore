from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import * 
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

def product_list(request):
    list_product = Product.objects.all()
    context = {
        'product_list': list_product
    }
    return render(request, 'shop/product/catalog.html', context)

def get_product_by_id(request, id):
    product_by_id = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        comment_form = FeebBack(request.POST)
        if comment_form.is_valid():
            review = comment_form.save(commit=False)
            review.user_name = request.user.username
            review.product = product_by_id
            review.save()
        else:
            context = {
                'form': comment_form,
                'product': product_by_id 
            }
            return render(request, 'shop/product/product_by_id.html', context)
            
    else:
        comment_form = FeebBack()
        context = {
            'form': comment_form,
            'product': product_by_id 
        }
        return render(request, 'shop/product/product_by_id.html', context)
    
    


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

@login_required
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
        product_create_form = ProductCreationForm(request.POST, request.FILES)
        if product_create_form.is_valid():
            product_create_form.save()
            return redirect('product_list')
        else:
            return render(request, 'shop/product/create_product.html', {'form': product_create_form})
    else:
        product_create_form = ProductCreationForm()
        return render(request, 'shop/product/create_product.html', {'form': product_create_form})
    
@login_required
def get_one_filter(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/catalog_with_filter.html', context)

@login_required
def get_more_filter_product(request):
    find_product = Product.objects.filter(
        price__lte = request.GET.get('max_price'),
        price__gt = request.GET.get('min_price')
    )
    context = {
        'find_product': find_product
    }

    return render(request, 'shop/product/catalog_with_filter.html', context)



class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True


class CreateSupplier(CreateView):
    model = Supplier
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class UpdateView(UpdateView):
    model = Supplier
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'shop/supplier/supplier_confirm_delete.html'
    success_url = reverse_lazy('product_filter_page')