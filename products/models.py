from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200) # may need some sort of array for category if we want to allow multiple categorizations
	
	def __str__(self):
		return self.name

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	description = models.TextField()
	shipping_speed = models.IntegerField(default=3)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='static/images', default='static/images/no-img.jpg') #FilePathField("/static/images", match="img.*")
	category = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	

