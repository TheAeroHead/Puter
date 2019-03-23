from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	shipping_speed = models.IntegerField(default=3)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	#category = models.ForeignKey(Category, on_delete=models.CASCADE) #ForeignKey field allows us to specify another class as a type

class Category(models.Model):
	name = models.CharField(max_length=200) # may need some sort of array for category if we want to allow multiple categorizations
