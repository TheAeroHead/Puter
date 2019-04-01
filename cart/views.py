from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Item
from .cart import Cart
from .forms import AddToCartForm


@require_POST
def cart_add(request, item_id):
	cart = Cart(request)
	item = get_object_or_404(Item, id=item_id)
	form = AddToCartForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
	return redirect('/cart/detail/')

@require_POST
def addCart(request):
	cart = Cart(request)
	item = request.POST['item']
	form = AddToCartForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
		for item in cart:
			item['update_quantity_form'] = AddToCartForm(initial={'quantity': item['quantity'], 'update': True})
			
	return render(request, 'cart/cart.html', {'cart': cart}) #redirect('cart:cart_detail')
	
def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('/cart/detail/')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = AddToCartForm(initial={'quantity': item['quantity'], 'update': True})
	context = {
		'cart': cart,
	}
	return render(request, 'cart/cart.html', context)
