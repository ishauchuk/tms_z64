from django.db import models


class Wh(models.Model):
    title = models.CharField(max_length=200, help_text="article name")
    amount = models.IntegerField(help_text="number of items")
    delivery_date = models.DateTimeField(auto_now_add=True)
    storage_time = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Warehouse'
        verbose_name_plural = 'Warehouses'



