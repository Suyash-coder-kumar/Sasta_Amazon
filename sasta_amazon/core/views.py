from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from products.models import Product
from cart.cart import SessionCart
from cart.models import Cart
# Create your views here.

def home(request):
    products=Product.objects.all()
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        items=cart.items.all()
        prod_dict={}
        for item in items:
            if not item.product.name in prod_dict:
                prod_dict[item.product.name]=item.quantity
    else:
        cart=SessionCart(request)
        prod_dict={}
        for item in cart.cart:
            if not item['product']['name'] in prod_dict:
                prod_dict[item['product']['name']]=item['quantity']
        
    return render(request,'core/home.html',{'products':products,'prod_dict':prod_dict})
