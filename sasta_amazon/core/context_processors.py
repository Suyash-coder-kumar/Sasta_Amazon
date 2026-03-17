from cart.models import Cart

def global_data(request):
    if request.user.is_authenticated:
        cart=Cart.objects.get(user=request.user)
        return {'counter':cart.cart_quantity}
    else:
        return {'counter':0}