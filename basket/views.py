from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shop.models import Product, Order, Pos_order
from .forms import BasketAddProductForm
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
    
