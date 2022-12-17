from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    desc = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    slug = models.SlugField()
    desc = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    address_one = models.CharField(max_length=30)
    address_two = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    phonenumber = models.SmallIntegerField()

    def __str__(self):
        return f"{self.__class__.__name__} object for {self.user}"


# Create your models here.
