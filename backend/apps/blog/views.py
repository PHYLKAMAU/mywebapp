from rest_framework import generics
from .models import Category, BlogPost
from .serializers import CategorySerializer, BlogPostListSerializer, BlogPostDetailSerializer

class CategoryListView(generics.ListAPIView):
    """List all blog categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BlogPostListView(generics.ListAPIView):
    """List all published blog posts"""
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostListSerializer

class BlogPostDetailView(generics.RetrieveAPIView):
    """Get single blog post details"""
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'

class FeaturedBlogPostListView(generics.ListAPIView):
    """List featured blog posts for homepage"""
    queryset = BlogPost.objects.filter(is_published=True, is_featured=True)
    serializer_class = BlogPostListSerializer

class CategoryBlogPostListView(generics.ListAPIView):
    """List blog posts by category"""
    serializer_class = BlogPostListSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return BlogPost.objects.filter(
            is_published=True,
            category__slug=category_slug
        )