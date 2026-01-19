from django.urls import path
from . import views
from .views import checkout, order_success

urlpatterns = [
    path('', views.product_list, name='products'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', order_success, name='order_success'),
    
]
