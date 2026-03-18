from django.shortcuts import get_object_or_404
from products.models import Product
class SessionCart():
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']=[]
        self.cart=cart
    
    def save(self):
        self.session.modified=True
    
    def add(self,product_id):
        product=get_object_or_404(Product,id=product_id)
        id=str(product_id)
        name=product.name
        price=str(product.price)
        image=product.image.url
        found=False
        for item in self.cart:
            if item['product']['id']==id:
                item['quantity']+=1
                found=True
                break
        
        if not found:
            self.cart.append({'product':{'id':id,'name':name,'price':price,'image':image},'quantity':1})
        self.save()
    
    def minus(self,product_id):
        id=str(product_id)
        for item in self.cart:
            if item['product']['id']==id :
                item['quantity']-=1
                break
        self.save()

    def remove(self,product_id):
        id=str(product_id)
        for item in self.cart:
            if item['product']['id']==id:
                self.cart.remove(item)
                break
        self.save()

    @property
    def cart_total(self):
        return sum(float(item['product']['price'])*item['quantity'] for item in self.cart)
        
    @property
    def cart_quantity(self):
        return sum(item['quantity'] for item in self.cart)