from rest_framework import serializers
from .models import Skill, Service, Project, Testimonial, About

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency', 'category', 'created_at']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'icon', 'description', 'features', 'price_range', 'is_featured', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'image', 'image_url', 'tech_stack', 
            'demo_url', 'github_url', 'case_study_url', 'is_featured', 
            'completed_date', 'created_at'
        ]
    
    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return "https://via.placeholder.com/400x300?text=Project+Image"

class TestimonialSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Testimonial
        fields = [
            'id', 'client_name', 'client_position', 'client_company', 
            'content', 'avatar', 'avatar_url', 'rating', 'is_featured', 'created_at'
        ]
    
    def get_avatar_url(self, obj):
        if obj.avatar and hasattr(obj.avatar, 'url'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return f"https://via.placeholder.com/100x100/cd5c2a/ffffff?text={obj.client_name[0] if obj.client_name else 'U'}"

class AboutSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    cv_file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = About
        fields = [
            'id', 'title', 'subtitle', 'bio', 'mission', 'profile_image', 
            'profile_image_url', 'years_experience', 'projects_completed', 
            'happy_clients', 'cv_file', 'cv_file_url', 'created_at', 'updated_at'
        ]
    
    def get_profile_image_url(self, obj):
        if obj.profile_image and hasattr(obj.profile_image, 'url'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.profile_image.url)
            return obj.profile_image.url
        return "https://via.placeholder.com/300x300/cd5c2a/ffffff?text=WK"
    
    def get_cv_file_url(self, obj):
        if obj.cv_file and hasattr(obj.cv_file, 'url'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cv_file.url)
            return obj.cv_file.url
        return None