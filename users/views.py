# users/views.py
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class LoginPageView(TemplateView):
	template_name = 'registration/login.html'
	
def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user) # tells auth to start a session and says the user is correctly authenticated
		return render(request, 'home.html') # redirects to payment page
	else:
		# user is invalid
		return render(request, 'registration/login.html') # reloads login page	
		