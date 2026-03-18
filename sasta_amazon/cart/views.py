from django.shortcuts import render,get_object_or_404,redirect
from cart.models import Cart,CartItem
from products.models import Product
from cart.cart import SessionCart
# Create your views here.

def cart(request):
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        items=cart.items.all()
    else:
        cart=SessionCart(request)
        items=cart.cart
    return render(request,'cart.html',{'cart':cart,'items':items})

def cart_add(request,product_id):
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        product=get_object_or_404(Product,id=product_id)
        cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
    else:
        cart=SessionCart(request)
        cart.add(product_id)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_minus(request,product_id):
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        product=get_object_or_404(Product,id=product_id)
        try:
            cart_item=CartItem.objects.get(cart=cart,product=product)
            if cart_item.quantity>1:
                cart_item.quantity-=1
                cart_item.save()
            else:
                cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    else:
        cart=SessionCart(request)
        for item in cart.cart:
            if item['product']['id'] == str(product_id): 
                if item['quantity'] > 1:
                    cart.minus(product_id)
                else:
                    cart.remove(product_id)
                break         

    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_remove(request,product_id):
    if request.user.is_authenticated:
        cart=get_object_or_404(Cart,user=request.user)
        product=get_object_or_404(Product,id=product_id)
        try:
            cart_item=CartItem.objects.get(cart=cart,product=product)
            cart_item.delete()
        except CartItem.DoesNotExist:
            pass
    else:
        cart=SessionCart(request)
        cart.remove(product_id)

    return redirect(request.META.get('HTTP_REFERER', '/'))

