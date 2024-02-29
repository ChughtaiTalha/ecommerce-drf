from django.contrib import admin
from .models import Product, Category, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'create_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'updated_at')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'category', 'quantity', 'price', 'status', 'create_at', 'updated_at')
