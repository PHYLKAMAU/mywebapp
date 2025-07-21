from rest_framework import serializers
from .models import ContactMessage, QuoteRequest

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value
    
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value.strip()
    
    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value.strip()

class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = [
            'name', 'email', 'company', 'budget', 'services', 
            'timeline', 'description'
        ]
    
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value
    
    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value.strip()
    
    def validate_description(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError("Please provide more details about your project (at least 20 characters).")
        return value.strip()
    
    def validate_services(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Please select at least one service.")
        return value