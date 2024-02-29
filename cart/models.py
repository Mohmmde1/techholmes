from django.db import models
from products.models import Product
from holmes_auth.models import User
from django.utils.text import slugify

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        # Calculate the total by iterating over all items in the cart
        total_amount = sum(item.product.price * item.quantity for item in self.items.all())
        return total_amount

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
