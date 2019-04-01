# payments/views.py
import stripe

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from products.models import Item, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from cart.cart import Cart
from orders.forms import OrderForm
from orders.models import OrderItem

# from payments.forms import OrderItemForm

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutPageView(TemplateView):
	template_name = 'cart/checkout.html'
	
	def get_context_data(self, **kwargs): 
		context = super().get_context_data(**kwargs)
		context['key'] = settings.STRIPE_PUBLISHABLE_KEY
		context['amount'] = request.POST['total_price']
		return context
		
def display(request):
	if request.method == 'POST':
		charge_amount = request.POST['total_price']
		context = {
			'amount': charge_amount,
			'key': settings.STRIPE_PUBLISHABLE_KEY
		}
		return render(request, 'orders/create.html', context) #render(request, 'cart/checkout.html', context)
	else:
		context = {
			'key': settings.STRIPE_PUBLISHABLE_KEY
		}
		response = HttpResponse("<center><h2>FATAL ERROR: Not a POST request.</h2></center>")
		return render(request, 'orders/create.html', context)
	
def charge(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		order = form.save()
		context = {
			'key': settings.STRIPE_PUBLISHABLE_KEY,
			'order': order,
		}
		for object in cart:
			OrderItem.objects.create(
				order=order,
				item=object['item'],
				price=object['price'],
				quantity=object['quantity']
			)
		cart.clear()
		#charge_amount = request.POST['amount']
		charge = stripe.Charge.create(
			amount=500,						#OrderItem.objects.filter(price__icontains(object['price'])),
			currency='usd', 				# will need to modify for different currency types (low priority)
			description='A New Django Order',
			source=request.POST['stripeToken']
		)
		return render(request, 'order_confirmation.html', context)
	else:
		response = HttpResponse("<center><h2>FATAL ERROR: Not a POST request.</h2></center>")
		return response
	
"""	
def order(request, pk):
	item_instance = get_object_or_404(ItemInstance, pk)
	
	# If this is a POST request then process the Form data
    if request.method == 'POST':
		form = OrderItemForm(request.POST)
		if form.is_valid(): 
			item_instance.delivery_date = form.cleaned_data['delivery_date']
			item_instance.save()
			
			# redirect to order confirmation page
			return HttpResponseRedirect(reverse('all-borrowed'))
	# If this is a GET request, then return default data	
	else:
		proposed_delivery_date = datetime.date.today() + datetime.timedelta(days=3)
        form = OrderItemForm(initial={'delivery_date': proposed_delivery_date})	
		
	context = {
		'form': form,
		'item_instance': item_instance,
	}
	
	return render(request, 'templates/order_confirmation.html', context)	
"""
