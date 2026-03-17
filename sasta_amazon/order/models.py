from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User
from products.models import Product
import uuid
# Create your models here.

class Order(BaseModel):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=models.ForeignKey(User,related_name="orders",on_delete=models.CASCADE)
    total=models.PositiveIntegerField()
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    @property
    def total(self):
        return sum(item.total for item in self.items.all())


class OrderItem(BaseModel):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order.user}-{self.product.name}({self.quantity})"
    
    @property
    def total(self):
        return(self.price*self.quantity)