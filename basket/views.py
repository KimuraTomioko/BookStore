from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shop.models import Product, Order, Pos_order
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', context={'basket': basket})


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
    return redirect('basket_detail')


@login_required
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('basket_detail')

    form = OrderForm(request.POST)
    if form.is_valid():
        # Создаём заказ, привязывая его к текущему пользователю
        order = Order.objects.create(
            user=request.user,  # Привязка к текущему пользователю
            buyer_lastname=form.cleaned_data['buyer_lastname'],
            buyer_name=form.cleaned_data['buyer_name'],
            buyer_surname=form.cleaned_data['buyer_surname'],
            comment=form.cleaned_data['comment'],
            delivery_type=form.cleaned_data['delivery_type'],
            delivery_address=form.cleaned_data['delivery_address']
        )

        # Проходим по товарам в корзине и создаём позиции заказа
        for item in basket:
            Pos_order.objects.create(
                product=item['product'],
                count=item['count'],
                order=order
            )

        # Очищаем корзину и перенаправляем пользователя
        basket.clear()
        return redirect('basket_detail')

    # Если форма не валидна, вернуть пользователя к корзине с сообщением об ошибке
    return render(request, 'basket/detail.html', {'form': form, 'basket': basket})



def open_order(request):
    context = {
        'form_order': OrderForm
    }
    return render(request, 'order/order_form.html', context=context)