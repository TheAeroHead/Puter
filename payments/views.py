# payments/views.py
import stripe

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from products.models import Item, Category

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
	template_name = 'home.html'
	
	def get_context_data(self, **kwargs): 
		context = super().get_context_data(**kwargs)
		context['key'] = settings.STRIPE_PUBLISHABLE_KEY
		return context
		
	
def charge(request):
	if request.method == 'POST':
		charge = stripe.Charge.create(
			amount=500,			# will need to modify for different charge amounts
			currency='usd', 	# will need to modify for different currency types (low priority)
			description='A Django charge',
			source=request.POST['stripeToken']
		)
		return render(request, 'charge.html')