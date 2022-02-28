from django.contrib import admin
from .models import Wh


@admin.register(Wh)
class WhAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'price', 'delivery_date', 'storage_time')
