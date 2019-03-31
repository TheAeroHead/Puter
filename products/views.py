from django.shortcuts import render
from django.views import generic
from .models import Item, Category
from django.http import HttpResponse
from .forms import ItemForm

class ItemListView(generic.ListView):
    model = Item
	#context_object_name = 'all_item_list'
	#queryset = Book.objects.filter()
	
def index(request):
	num_items = Item.objects.count()
	num_categories = Category.objects.count()
	context = {
        'num_items': num_items,
		'num_categories': num_categories,
    } # Python dictionary holds all variables to be inserted into index.html template
	return render(request, 'index.html', context=context)

def faq(request):
    return render(request, 'faq.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def hello(request):
	response = HttpResponse("<center><h2>Welcome to the page at %s</h2></center>" % request.path)
	user_info = request.META.get('HTTP_USER_AGENT', 'unknown')
	user_ip = request.META.get('REMOTE_ADDR', 'unknown')
	response.write("<center>Your browser is %s</center>" % user_info)
	response.write("<br><center>Your IP address is %s</center>" % user_ip)
	return response
# https://djangobook.com/django-forms/ helpful tutorial for forms which we will be using heavily on this project.
# Above tutorial uses a deprecated routing schema (url instead of path). 
# Compare the url file for path('hello') to their example to better understand difference.
	
def search_form(request):
	return render(request, 'products/search_form.html')
	
def search_result(request):
	error = False
	if 'query' in request.GET:
		query = request.GET['query']
		if not query:
			error = True
		else:
			message = "<center><h2>Search results for: %r</h2></center>" % request.GET['query']
			items = Item.objects.filter(name__icontains=query)
			context = {
				'query': query,
				'items': items,
			}
			return render(request, 'products/search_result.html', context)
	else:
		message = "<center><h2>You searched with an empty field. Please enter a search term</h2></center>"
		# Deprecated response to return message statement: return HttpResponse(message)
		return render(request, 'products/search_form.html', {'error':error}) 

def add_item(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			#id = form.cleaned_data['id']
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			shipping_speed = form.cleaned_data['shipping_speed']
			price = form.cleaned_data['price']
			category = form.cleaned_data['category']
			#image = form.cleaned_data['image']
			
			new_item = Item.objects.create(name = name, 
										description = description, 
										shipping_speed = shipping_speed, 
										price = price,
										#id = id,
										category = category,
										#image = image,
										) 
			#new_item.set(category)
			new_item.save()
			return HttpResponse("Created new object")
	
	else:
		form = ItemForm() # a blank form if not a POST request.

	return render(request, 'products/add_item.html', {'form': form}) #HttpResponse("Missing object data")