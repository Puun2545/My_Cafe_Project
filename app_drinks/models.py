from django.db import models

# Create your models here.

class Drink(models.Model):

    title = models.CharField(max_length=60)
    price = models.IntegerField()
    promotion_price = models.IntegerField(null=True)
    is_premium = models.BooleanField(default=False)
    promotion_end_at = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    