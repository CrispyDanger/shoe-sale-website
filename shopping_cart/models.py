from django.conf import settings
from django.db import models

from shopping.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)


# Create your models here.
