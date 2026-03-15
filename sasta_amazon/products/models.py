from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Category(BaseModel):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Product(BaseModel):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    
