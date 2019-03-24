# products/forms.py
from django import forms

class ItemForm(forms.Form):
	name = models.CharField(max_length=200)
	description = models.TextField()
	shipping_speed = models.IntegerField(default=3)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField()