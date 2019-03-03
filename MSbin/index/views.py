from django.shortcuts import render
from .models import Paste

def home(request):
	context = {'pastes': Paste.objects.all()}
	return render(request, 'index/home.html', context)

def about(request):
	return render(request, 'index/about.html', {'title': 'test'})
