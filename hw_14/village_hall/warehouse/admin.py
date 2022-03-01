from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'price', 'delivery_date', 'storage_time']
    list_editable = ['amount', 'price']
    list_filter = ['price', 'amount']
    ordering = ['-delivery_date']
    list_per_page = 3
