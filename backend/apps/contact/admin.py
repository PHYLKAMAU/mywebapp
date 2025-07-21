from django.contrib import admin
from .models import ContactMessage, QuoteRequest

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'get_subject_display', 'is_read', 'created_at']
    list_filter = ['subject', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"
    
    actions = [mark_as_read, mark_as_unread]

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'get_budget_display', 'get_timeline_display', 'is_processed', 'created_at']
    list_filter = ['budget', 'timeline', 'is_processed', 'created_at']
    search_fields = ['name', 'email', 'company', 'description']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'email', 'company')
        }),
        ('Project Details', {
            'fields': ('budget', 'timeline', 'services', 'description')
        }),
        ('Status', {
            'fields': ('is_processed', 'created_at')
        }),
    )
    
    def mark_as_processed(self, request, queryset):
        queryset.update(is_processed=True)
    mark_as_processed.short_description = "Mark selected quotes as processed"
    
    def mark_as_unprocessed(self, request, queryset):
        queryset.update(is_processed=False)
    mark_as_unprocessed.short_description = "Mark selected quotes as unprocessed"
    
    actions = [mark_as_processed, mark_as_unprocessed]