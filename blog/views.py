from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
	context_object_name = 'posts_list'
	model = Post
	template_name = 'home.html'

class PostDetailView(DetailView):
	context_object_name = 'post_detail'
	model = Post 
	template_name = 'detail.html'

class PostCreateView(CreateView):
	model = Post 
	template_name = 'new_post.html'
	fields = ('title','author','body')

class PostUpdateView(UpdateView):
	model = Post 
	template_name = 'update.html'
	fields = ('title','body')

class PostDeleteView(DeleteView):
	model = Post 
	template_name = 'delete.html'
	success_url = reverse_lazy('home')