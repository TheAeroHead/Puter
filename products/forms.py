# products/forms.py
from django import forms

class ItemForm(forms.Form):
	#id = forms.AutoField()
	name = forms.CharField(max_length=200)
	description = forms.CharField(widget=forms.Textarea)
	shipping_speed = forms.IntegerField() #max_digits=6, decimal_places=2
	price = forms.DecimalField(max_digits=6, decimal_places=2) 
	#category = forms.CharField(max_length=200)
	#image = forms.ImageField()