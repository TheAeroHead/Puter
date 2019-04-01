from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200) # may need some sort of array for category if we want to allow multiple categorizations
	
	class Meta:
		ordering = ('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.name

class Item(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, db_index=True)
	description = models.TextField()
	shipping_speed = models.IntegerField(default=3)
	price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
	image = models.ImageField(upload_to="images", default="images/no-img.jpg") #FilePathField("/static/images", match="img.*")
	category = models.CharField(max_length=200, db_index=True) #models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
	
class Order(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=200)
	quantity = models.PositiveIntegerField()
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __str__(self):
		return self.id

