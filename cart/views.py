from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST # Добавлен при создании формы для карзины
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Эта вьюха добавляет товар в корзину. В качестве параметра она принимает запрос и идентификатор товара.
# Здесь мы используем декоратор require_POST для того, чтобы принимать только POST запросы
@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:CartDetail')


# для удаления товаров из корзины
def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


# Эта функция получает экземпляр корзины пользователя и передает его в качестве параметра в шаблон
def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                                'quantity': item['quantity'],
                                                                'update': True
                                                                })
    return render(request, 'cart/detail.html', {'cart': cart})