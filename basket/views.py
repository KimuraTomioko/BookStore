from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shop.models import Product, Order, Pos_order
from .forms import BasketAddProductForm, OrderForm
from .basket import Basket

def basket_detail(request):
    basket = Basket(request)
    context = {
        'basket': basket
    }
    return render(request, 'basket/detail.html')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['update']
        )
    return redirect('basket_detail')

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')
    
def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_details')

@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('basket_detail')
    
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(buyer_name=form.cleaned_data['buyer_name'],
                                     buyer_surname = form.cleaned_data['buyer_surname'],
                                     buyer_firstname = form.cleaned_data['buyer_firstname'],
                                     comment = form.cleaned_data['comment'],
                                     delivery_type = form.cleaned_data['delivery_type'],
                                     delivery_address = form.cleaned_data['delivery_address'])
        order.price = basket.get_total_price_position()
        for item in basket:
            pos_order = Pos_order.objects.create(
                product = item['product'],
                count=item['count'],
                order = order
            )
        basket.clear()
    return redirect('basket_detail')