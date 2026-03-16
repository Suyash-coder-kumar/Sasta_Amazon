from django.urls import path
from . import views
urlpatterns=[
    path('',views.cart,name="cart"),
    path('add/',views.cart_add,name="cart_add"),
    path('minus/',views.cart_minus,name="cart_minus"),
    path('remove/',views.cart_remove,name="cart_remove"),
]