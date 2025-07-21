from django.urls import path
from .views import (
    SkillListView, ServiceListView, ProjectListView,
    FeaturedProjectListView, ProjectDetailView, TestimonialListView, 
    AboutView, skills_by_category, portfolio_stats
)

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='skills-list'),
    path('skills/by-category/', skills_by_category, name='skills-by-category'),
    path('services/', ServiceListView.as_view(), name='services-list'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('projects/featured/', FeaturedProjectListView.as_view(), name='featured-projects'),
    path('projects/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonials-list'),
    path('about/', AboutView.as_view(), name='about'),
    path('stats/', portfolio_stats, name='portfolio-stats'),
]