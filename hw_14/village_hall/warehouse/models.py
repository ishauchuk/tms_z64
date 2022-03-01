from django.db import models
from django.core.validators import ValidationError
from datetime import date


def validate_storage_time(storage_time):
    today = date.today()
    if today > storage_time:
        raise ValidationError("The expiration date can`t be in the past!")


class Product(models.Model):

    CURRENCY_CHOICES = [
        ('BYN', 'Rubles'),
        ('USD', 'Dollars'),
        ('EUR', 'Euro'),
    ]

    title = models.CharField(max_length=200, help_text="article name", )
    amount = models.IntegerField(help_text="number of items")
    delivery_date = models.DateTimeField(auto_now_add=True)
    storage_time = models.DateField(validators=[validate_storage_time])
    price = models.DecimalField(max_digits=8, decimal_places=2, max_length=3, choices=CURRENCY_CHOICES, default='BYN')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'




