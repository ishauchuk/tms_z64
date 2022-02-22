from django.db import models


class Coins(models.Model):
    title = models.CharField('Coin name', max_length=50)
    price = models.FloatField('Coin price', default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'

