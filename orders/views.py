from django.shortcuts import render
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.conf import settings
import stripe

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
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
        return render(request, 'orders/created.html', context)
    else:
        form = OrderForm()
        context = {
            'key': settings.STRIPE_PUBLISHABLE_KEY,
		    'form': form,
        }
    return render(request, 'orders/create.html', context)