from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Site Product
def ProductList(request, category_slug=None): # category_slug - параметр, который будет фильтровать товары по категории
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) #available=True - получаем только те товары, которые в наличаи.
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
        })

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {
        'product': product
        })

