# payments/urls.py
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	path('charge/', views.charge, name='charge'),
	path('checkout/', views.CheckoutPageView.as_view(), name='home'),
	path('', views.display),
	#path('', RedirectView.as_view(url='/index/', permanent=True)),
	#path('', views.index, name='index'),
]
