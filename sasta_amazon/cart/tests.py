from django.test import TestCase
from django.contrib.auth import get_user_model
from cart.models import Cart, CartItem
from products.models import Product,Category
import uuid

User = get_user_model()


class CartModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser",password="testpass123")
        self.cart = Cart.objects.create(user=self.user)
        electronics = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(id=uuid.uuid4(),name="Laptop",slug="laptop",category=electronics,price=50000.00,description="High performance laptop",)
        self.phone = Product.objects.create(id=uuid.uuid4(),name="Smartphone",slug="smartphone",category=electronics,price=20000.00,description="Latest smartphone",)

    def test_cart_item_creation(self):
        item = CartItem.objects.create(cart=self.cart,product=self.product,quantity=2)
        self.assertEqual(item.quantity, 2)
        self.assertEqual(item.product.name, "Laptop")

    def test_total_price_property(self):
        item = CartItem.objects.create(cart=self.cart,product=self.product,quantity=3)
        self.assertEqual(item.total_price, 150000)

    def test_cart_total(self):
        CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)
        CartItem.objects.create(cart=self.cart, product=self.phone, quantity=1)
        self.assertEqual(self.cart.cart_total, 120000)