from django.db import models

# Create your models here.
class CustomUser(models.Model):
	username = models.EmailField(max_length=200)
	
