from django.urls import path
from . import views

urlpatterns=[
    path('',views.creat_order,name='create_order'),
    path('myorders/',views.user_order,name='user_order'),
    path('success/<uuid:order_id>/',views.success_order,name='success_order')
]