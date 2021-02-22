from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

class PostListView(ListView):
	context_object_name = 'posts_list'
	model = Post
	template_name = 'home.html'

class PostDetailView(DetailView):
	context_object_name = 'post_detail'
	model = Post 
	template_name = 'detail.html'