from django.shortcuts import render,redirect
from order.models import Order,OrderItem
from cart.models import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def creat_order(request):
    user=request.user
    cart=Cart.objects.get(user=user)
    order=Order.objects.create(user=user)
    created=False

    for item in cart.items.all():
        if item.product.stock>=item.quantity:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
                )
            item.product.stock-=item.quantity
            item.product.save()
            created=True
    if created:
        cart.items.all().delete()
        return redirect('success_order',order_id=order.id)
    else:
        return redirect('cart')

    

@login_required    
def success_order(request,order_id):
    return render(request,'order/success.html')

@login_required
def user_order(request):
    orders=Order.objects.filter(user=request.user)
    return render(request,'order/myorder.html',{'orders':orders})