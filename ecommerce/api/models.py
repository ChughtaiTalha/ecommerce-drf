import uuid

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Category(BaseModel):
    name = models.CharField(max_length=150, unique=True)


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")])
