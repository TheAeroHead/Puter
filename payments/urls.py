# payments/urls.py
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	path('charge/', views.charge, name='charge'),
	path('', views.HomePageView.as_view(), name='home'),
	#path('', RedirectView.as_view(url='/index/', permanent=True)),
	#path('', views.index, name='index'),
]
