# products/urls.py
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	#path('charge/', views.charge, name='charge'),
	#path('', views.HomePageView.as_view(), name='home'),
	#path('', RedirectView.as_view(url='/index/', permanent=True)),
	path('', views.index, name='index'),
	path('hello', views.hello, name='hello'),
	path('search_form', views.search_form, name='search_form'),
	path('search_result', views.search_result, name='search_result'),
	path('add_item', views.add_item, name='add_item'),
	path('product_detail', views.product_detail, name='product_detail'),
    path('faq', views.faq, name='faq'),
    path('contact_us', views.contact_us, name='contact_us'),
	path('cart', views.cart, name='cart'),
	path('profile_info', views.profile_info, name='profile_info'),
	#path('viewItem', views.ItemListView.as_view(), name='viewItem'),
	#path('', views.ItemListView.as_view(), name='Items'),
]