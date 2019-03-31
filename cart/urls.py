# /cart/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
	#path('', RedirectView.as_view(url='index/cart', permanent=True)),
	path('', views.cart_detail),
	path('add', views.cart_add),
	path('remove', views.cart_remove),
	path('checkout', include('payments.urls')),
]
