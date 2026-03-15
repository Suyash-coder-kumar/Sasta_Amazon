from django.contrib import admin
from products.models import Product,Category
# Register your models here.

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','price','created_at')
    prepopulated_fields=({'slug':('name',)})
    list_filter=('category',)