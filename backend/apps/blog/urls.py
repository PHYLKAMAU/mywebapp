from django.urls import path
from .views import (
    CategoryListView, BlogPostListView, BlogPostDetailView, 
    FeaturedBlogPostListView, CategoryBlogPostListView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='blog-categories'),
    path('posts/', BlogPostListView.as_view(), name='blog-posts'),
    path('posts/featured/', FeaturedBlogPostListView.as_view(), name='featured-blog-posts'),
    path('posts/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('category/<slug:category_slug>/', CategoryBlogPostListView.as_view(), name='category-blog-posts'),
]