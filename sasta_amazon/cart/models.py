from django.db import models
from products.models import Product
from core.models import BaseModel
import uuid
from django.conf import settings
# Create your models here.

class Cart(BaseModel):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    @property
    def cart_total(self):
        return sum(item.total_price for item in self.items.all())
    @property
    def cart_quantity(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    class Meta:
        unique_together=('cart','product')

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
    @property
    def total_price(self):
        return self.product.price*self.quantity
