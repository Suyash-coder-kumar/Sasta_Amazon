from django.shortcuts import render,get_object_or_404,redirect
from cart.models import Cart,CartItem
from products.models import Product

# Create your views here.

def cart(request):
    user=request.user
    cart=get_object_or_404(Cart,user=user)
    items=cart.items.all()
    return render(request,'cart.html',{'cart':cart,'items':items})

def cart_add(request,product_id):
    user=request.user
    cart=get_object_or_404(Cart,user=user)
    product=get_object_or_404(Product,id=product_id)
    cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
    if not created:
        cart_item.quantity+=1
        cart_item.save()
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_minus(request,product_id):
    user=request.user
    cart=get_object_or_404(Cart,user=user)
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

    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_remove(request,product_id):
    user=request.user
    cart=get_object_or_404(Cart,user=user)
    product=get_object_or_404(Product,id=product_id)
    try:
        cart_item=CartItem.objects.get(cart=cart,product=product)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect(request.META.get('HTTP_REFERER', '/'))

