from django.shortcuts import render,redirect
from order.models import Order,OrderItem
from cart.models import Cart

# Create your views here.
def creat_order(request):
    user=request.user
    cart=Cart.objects.get(user=user)

    order=Order.objects.create(user=user)

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
            )

        cart.items.all().delete()
    
    return redirect('success_order')
    
def success_order(request):
    return render(request,'order/success.html')
