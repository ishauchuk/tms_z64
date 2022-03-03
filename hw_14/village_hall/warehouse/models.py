from django.db import models
from django.core.validators import ValidationError
from datetime import date

today = date.today()


def validate_storage_time(storage_time):
    if today > storage_time:
        raise ValidationError("The expiration date can`t be in the past!")


class Product(models.Model):
    BYN = 'BYN'
    USD = 'USD'
    EUR = 'EUR'
    CURRENCY_CHOICES = [
        (BYN, 'Rubles'),
        (USD, 'Dollars'),
        (EUR, 'Euro'),
    ]

    title = models.CharField(max_length=200, help_text="article name", )
    amount = models.IntegerField(help_text="number of items")
    delivery_date = models.DateTimeField(auto_now_add=True)
    storage_time = models.DateField(validators=[validate_storage_time])
    price = models.FloatField(help_text="price in BYN")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES,
                                default='BYN')

    def __str__(self):
        return self.title

    def currency_amount(self):
        if self.currency == self.USD:
            return round(self.price / 3, 2)
        elif self.currency == self.EUR:
            return round(self.price / 3.5, 2)
        else:
            return self.price

    currency_amount.short_description = 'Price in currency'

    def currency_vat(self):
        return round(self.currency_amount() * 1.2, 2)

    currency_vat.short_description = 'Price with vat'

    def currency_discount(self):
        if int(str(self.storage_time - today).split()[0]) < 10:
            return round(self.currency_amount() * 0.7, 2)
        else:
            return 'no discount'

    currency_discount.short_description = 'Price with discount'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
