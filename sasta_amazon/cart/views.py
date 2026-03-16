from django.shortcuts import render
from cart.models import Cart,CartItem
# Create your views here.

def cart(request):
    user=request.user
    cart=Cart.objects.get(user=user)
    items=cart.items.all()
    return render(request,'cart.html',{'cart':cart,'items':items})

def cart_add(request):
    pass

def cart_minus(request):
    pass

def cart_remove(request):
    pass