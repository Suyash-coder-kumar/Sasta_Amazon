from django.urls import path
from . import views

urlpatterns=[
    path('',views.creat_order,name='create_order'),
    path('success/',views.success_order,name='success_order')
]