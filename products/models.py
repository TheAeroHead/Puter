from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=255) # will need to use some other model type to increase size (charfield max is like 256 I think)
	shipping_speed = models.IntegerField(default=3)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	category = models.CharField(max_length=200) # may need some sort of array for category if we want to allow multiple categorizations
