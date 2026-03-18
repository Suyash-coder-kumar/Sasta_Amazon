from cart.models import Cart
from cart.cart import SessionCart
from django.shortcuts import get_object_or_404

def global_data(request):
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        return {'counter':cart.cart_quantity}
    else:
        cart=SessionCart(request)
        return {'counter':cart.cart_quantity}