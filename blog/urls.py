from django.urls import path

from . import views 


urlpatterns = [
	path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name = 'delete'),
	path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name = 'update'),
	path('post/detail/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'),
	path('post/create/', views.PostCreateView.as_view(), name = 'new-post'),
	path('', views.PostListView.as_view(), name = 'home'),
	
	
	
]