from django.db import models
from django.contrib import auth

class Supply(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    barcode = models.BigIntegerField(null=False)
    quantity = models.IntegerField(default=1, null=False)
    price = models.IntegerField(default=0, null=False)
    supply_time = models.DateTimeField(null=False)
    class Meta:
        indexes = [
            models.Index(fields=['barcode', 'supply_time']),
        ]

    def __str__(self):
        return self.id

class Sale(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    barcode = models.BigIntegerField(null=False)
    quantity = models.IntegerField(default=1, null=False)
    price = models.IntegerField(default=0, null=False)
    sale_time = models.DateTimeField(auto_now_add=True, null=False)
    class Meta:
        indexes = [
            models.Index(fields=['barcode', 'sale_time']),
        ]

    def __str__(self):
        return self.id