from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.

def blog_home(request):
	'''List top 10 posts and display other things'''
	all_posts = BlogPost.objects.all()
	return render(request, 'blog/bloghome.html', {'all_posts':all_posts})

def blog_detail(request, slug):
	'''detailed view - full article'''
	blog_detail = get_object_or_404(BlogPost, slug=slug)
	return render(request, 'blog/blogdetail.html', {'blog_detail':blog_detail})

