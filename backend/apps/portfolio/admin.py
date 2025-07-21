from django.contrib import admin
from .models import Skill, Service, Project, Testimonial, About

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name']
    ordering = ['category', 'name']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'proficiency')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_featured', 'price_range', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['title', 'description']
    ordering = ['-is_featured', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'icon', 'description')
        }),
        ('Details', {
            'fields': ('features', 'price_range', 'is_featured')
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'completed_date', 'created_at']
    list_filter = ['is_featured', 'completed_date', 'created_at']
    search_fields = ['title', 'description']
    date_hierarchy = 'completed_date'
    ordering = ['-is_featured', '-completed_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Technical Details', {
            'fields': ('tech_stack',)
        }),
        ('Links', {
            'fields': ('demo_url', 'github_url', 'case_study_url')
        }),
        ('Settings', {
            'fields': ('is_featured', 'completed_date')
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Add help text for tech_stack field
        if 'tech_stack' in form.base_fields:
            form.base_fields['tech_stack'].help_text = 'Enter as JSON array, e.g., ["React", "Node.js", "MongoDB"]'
        return form

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'client_position', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured', 'created_at']
    search_fields = ['client_name', 'client_company', 'content']
    ordering = ['-is_featured', '-created_at']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_position', 'client_company', 'avatar')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Settings', {
            'fields': ('is_featured',)
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'years_experience', 'projects_completed', 'happy_clients', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subtitle', 'profile_image')
        }),
        ('Content', {
            'fields': ('bio', 'mission')
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_completed', 'happy_clients')
        }),
        ('Documents', {
            'fields': ('cv_file',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one About instance
        return not About.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of About instance
        return False