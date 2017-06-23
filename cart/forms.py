from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int) # поле предназначено для выбора количества товара
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput) # поле проверяет если товар ранее был добавлен в корзину