from django.shortcuts import render
from products.models import Product, Category

# Create your views here.
def shop(request):
    products=Product.objects.all()
    return render(request,'shop/shop.html',{'products':products})
