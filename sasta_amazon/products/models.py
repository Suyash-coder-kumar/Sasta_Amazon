from django.db import models
from core.models import BaseModel
import uuid

# Create your models here.

class Category(BaseModel):
    name=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="Categories"
        db_table="Category table"

    def __str__(self):
        return self.name


class Product(BaseModel):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to="core",null=True,blank=True)

    class Meta:
        verbose_name_plural="Products"
        db_table="Product table"

    def __str__(self):
        return self.name
    
