from django.shortcuts import render

posts = [
	{
		'author': 'alalim',
		'title': 'post 1',
		'content': 'hello',
		'date': 'March 2, 2019'
	},
	{
		'author': 'sohailaw',
		'title': 'post 2',
		'content': 'world',
		'date': 'March 3, 2019'
	}
]

def home(request):
	context = {'posts': posts}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'test'})