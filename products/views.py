from django.shortcuts import render
from django.views import generic
from .models import Item, Category

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