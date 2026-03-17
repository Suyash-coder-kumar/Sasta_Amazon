from django.shortcuts import render,get_object_or_404
from products.models import Product, Category
from cart.models import Cart

# Create your views here.
def shop(request):
    products=Product.objects.all()
    cart=get_object_or_404(Cart,user=request.user)
    items=cart.items.all()
    prod_dict={}
    for item in items:
        if not item.product.name in prod_dict:
            prod_dict[item.product.name]=item.quantity
    return render(request,'shop/shop.html',{'products':products,'prod_dict':prod_dict})
