from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('accessories', 'Accessories'),
        ('wearables', 'Wearables'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='electronics'
    )
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    PAYMENT_CHOICES = (
        ('COD', 'Cash on Delivery'),
        ('UPI', 'UPI'),
        ('BANK', 'Bank Transfer'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_CHOICES,
        default='COD'   # IMPORTANT
    )
    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
