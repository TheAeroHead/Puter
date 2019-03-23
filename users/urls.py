# users/urls.py
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
	#path('login/', views.login, name='login'),
	path('', include('django.contrib.auth.urls')),
	#path('', views.LoginPageView.as_view(), name='login'),
]