# products/forms.py
from django import forms
from django.utils.safestring import mark_safe
"""
class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
		html =  Template(<img src="$link"/>)
		
	return mark_safe(html.substitute(link=value)
"""
class ItemForm(forms.Form):
	#id = forms.AutoField()
	name = forms.CharField(max_length=200)
	description = forms.CharField(widget=forms.Textarea)
	shipping_speed = forms.IntegerField() #max_digits=6, decimal_places=2
	price = forms.DecimalField(max_digits=6, decimal_places=2) 
	category = forms.CharField(max_length=200)
	#image = forms.ImageField()