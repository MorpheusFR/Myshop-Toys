from decimal import Decimal # Для уточнения цены
from django.conf import settings
from shop.models import Product


class Cart(object): # Класс для работы с карзиной по средствам сессий
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
# Сессии мы получаем через запрос, после чего мы проверяем если есть сессия с нашим идентификатором 'cart' и если ее нет, то мы устанавливаем ее.


    def add(self, product, quantity=1, update_quantity=False): # Добавляет товар в корзину пользователя или обновляет количество товара
    # Метод add() получает в качестве параметром товар (product), количество товара (quantity), а также логическое значение update_quantity, которое принимает True, если товар ранее уже был добавлен.
        product_id = str(product.id) # product_id используется для идентификации товара
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self): # Сохранение данных в сессию
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True # Указываем что сессия изменена


    def remove(self, product): # Удаление продуктов из корзины
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self): # Итерация по товарам
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self): # Количество товаров
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self): # для получения полной стоимости товаров
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())


    def clear(self): # для очистки сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True