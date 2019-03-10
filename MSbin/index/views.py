from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Paste

def home(request):
	context = {'pastes': Paste.objects.all()}
	return render(request, 'index/home.html', context)

class PasteListView(ListView):
	model = Paste
	template_name = 'index/home.html'
	context_object_name = 'pastes'
	ordering = ['-date']

class PasteDetailView(DetailView):
	model = Paste


def about(request):
	return render(request, 'index/about.html', {'title': 'test'})
