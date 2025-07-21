from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Skill, Service, Project, Testimonial, About
from .serializers import (
    SkillSerializer, ServiceSerializer, ProjectSerializer,
    TestimonialSerializer, AboutSerializer
)

class SkillListView(generics.ListAPIView):
    """List all skills grouped by category"""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ServiceListView(generics.ListAPIView):
    """List all services"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ProjectListView(generics.ListAPIView):
    """List all projects"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class FeaturedProjectListView(generics.ListAPIView):
    """List only featured projects"""
    queryset = Project.objects.filter(is_featured=True)
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    """Get single project details"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'

class TestimonialListView(generics.ListAPIView):
    """List featured testimonials"""
    queryset = Testimonial.objects.filter(is_featured=True)
    serializer_class = TestimonialSerializer

class AboutView(generics.RetrieveAPIView):
    """Get about information"""
    serializer_class = AboutSerializer

    def get_object(self):
        # Get the first (and should be only) About instance
        about_instance = About.objects.first()
        if not about_instance:
            # Create default about instance if none exists
            about_instance = About.objects.create(
                title="About Wambui Kamau",
                subtitle="Full-Stack Developer & IT Solutions Expert",
                bio="Passionate developer with expertise in modern web technologies.",
                mission="To deliver innovative technology solutions that drive business growth.",
                years_experience=5,
                projects_completed=50,
                happy_clients=30
            )
        return about_instance

@api_view(['GET'])
def skills_by_category(request):
    """Get skills grouped by category"""
    categories = Skill.CATEGORY_CHOICES
    result = {}
    
    for category_value, category_label in categories:
        skills = Skill.objects.filter(category=category_value)
        result[category_value] = {
            'label': category_label,
            'skills': SkillSerializer(skills, many=True, context={'request': request}).data
        }
    
    return Response(result)

@api_view(['GET'])
def portfolio_stats(request):
    """Get portfolio statistics"""
    about = About.objects.first()
    stats = {
        'years_experience': about.years_experience if about else 0,
        'projects_completed': about.projects_completed if about else Project.objects.count(),
        'happy_clients': about.happy_clients if about else 0,
        'total_projects': Project.objects.count(),
        'total_skills': Skill.objects.count(),
        'total_services': Service.objects.count(),
    }
    return Response(stats)