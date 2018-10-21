from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def blog_home(request):
	'''List top 10 posts and display other things'''
	all_posts = BlogPost.objects.all()
	return render(request, 'blog/bloghome.html', {'all_posts':all_posts})

def blog_detail(request):
	'''detailed view - full article'''
	pass

def blog_list(request):
	'''list all blog posts published'''
	pass