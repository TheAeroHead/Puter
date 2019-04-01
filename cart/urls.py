# /cart/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView

from . import views

app_name = 'cart'

urlpatterns = [
	#path('', RedirectView.as_view(url='index/cart', permanent=True)),
	#path('add/<int:item_id>', views.cart_add, name = 'cart_add'),
	#path('add', views.cart_add, name = 'cart_add'),
	url(r'^add/(?P<item_id>\d+)/$', views.cart_add, name='cart_add'),
	url(r'^remove/(?P<item_id>\d+)/$', views.cart_remove, name='cart_remove'),
	path('detail/', views.cart_detail, name='cart_detail'),
	#path('remove', views.cart_remove, name='cart_remove'),
	path('checkout', include('payments.urls')),
	path('cart', views.cart_detail),
	path('', views.cart_detail, name='cart'),
]
