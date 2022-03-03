from django.contrib import admin
from .models import Product
from django.db.models import QuerySet


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['currency']
    list_display = ['title', 'amount', 'price', 'currency', 'currency_amount',
                    'currency_vat', 'delivery_date', 'storage_time',
                    'currency_discount']
    list_editable = ['amount', 'price', 'currency']
    list_filter = ['price', 'amount']
    ordering = ['-delivery_date']
    list_per_page = 3
    actions = ['set_to_dollars', 'set_to_euro', 'set_to_byn']

    @admin.action(description='Set the dollars')
    def set_to_dollars(self, request, QuerySet):
        QuerySet.update(currency=Product.USD)

    @admin.action(description='Set the euro')
    def set_to_euro(self, request, QuerySet):
        QuerySet.update(currency=Product.EUR)

    @admin.action(description='Set the byn')
    def set_to_byn(self, request, QuerySet):
        QuerySet.update(currency=Product.BYN)
