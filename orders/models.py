from django.db import models
from holmes_auth.models import User
from products.models import Product
from cart.models import Cart


class Order(models.Model):
    # Define choices for status
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
            return f"by {self.user.email} - Status: {self.status}, Total: {self.total}"
