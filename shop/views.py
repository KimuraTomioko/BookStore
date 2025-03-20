from django.shortcuts import redirect, render, get_object_or_404

from basket.forms import BasketAddProductForm
from .models import *
from .forms import * 
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .utils import CalculateMoney

def product_list(request):
    list_orders = Order.objects.all()
    context = {
        'order_list': list_orders
    }
    return render(request, 'shop/product/catalog.html', context)

def get_product_by_id(request, id):
    product_by_id = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        if Review.objects.filter(product=product_by_id, user = request.user).exists():
            messages.error(request, 'Вы не можете оставить более 1 отзыва под товаром!')
            return redirect('product_filter_page')
    
        comment_form = FeebBack(request.POST)
        if comment_form.is_valid():
            review = comment_form.save(commit=False)
            review.user = request.user
            review.product = product_by_id
            review.save()
            messages.success(request, 'Ваш отзыв был успешно оставлен!')
            return redirect('product_filter_page')
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
        'find_product': find_product,
    }

    return render(request, 'shop/product/filter.html', context)

def get_one_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        'form_basket': BasketAddProductForm
    }
    return render(request, 'shop/product/one_product.html', context)

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
    
    search_query = request.GET.get('search')
    if search_query:
        list_product = list_product.filter(name__icontains=search_query)
        
        
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



#suppliers
class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True
    paginate_by = 3

class CreateSupplier(CreateView):
    model = Supplier
    extra_context = {
        'action':'Создать'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class UpdateSupplier(UpdateView):
    model = Supplier
    extra_context = {
        'action':'Изменить'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm

class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'

class DeleteSupplier(DeleteView):
    model = Supplier
    template_name = 'shop/supplier/supplier_confirm_delete.html'
    success_url = reverse_lazy('product_filter_page')

class AddWarehouse(CreateView):
    model = Warehouse
    form_class = AddWarehouseForm
    template_name = 'shop/warehouse/add_warehouse.html'


#orders
class OrderDetail(DetailView, CalculateMoney):
    model = Order
    template_name = 'shop/order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        order = context.get('object')

        list_price = [pos_order.sum_price_count() for pos_order in order.pos_order_set.all()]

        context['sum_price'] = self.sum_price(prices=list_price)
        return context

    

@login_required
class CreateOrder(CreateView):
    model = Order
    extra_context = {
        'action':'Создать'
    }
    template_name = 'shop/order/create.html'
    form_class = AddOrder

@login_required
class UpdateOrder(UpdateView):
    model = Order
    extra_context = {
        'action': 'Обновить'
    }
    template_name = 'shop/order/update.html'

@login_required
class DeleteOrder(DeleteView):
    model = Order
    template_name = 'shop/order/confirm_delete.html'
    reverse_lazy = reverse_lazy('order_page')


#review
class UpdateRating(UpdateView):
    model = Review
    form_class = FeebBack
    template_name = 'product_by_id.html'



            
