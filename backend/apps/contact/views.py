from rest_framework import generics, status
from rest_framework.response import Response
from .models import ContactMessage, QuoteRequest
from .serializers import ContactMessageSerializer, QuoteRequestSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    """Create a new contact message"""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {
                "message": "Thank you for your message! I'll get back to you within 24 hours.",
                "success": True
            },
            status=status.HTTP_201_CREATED
        )

class QuoteRequestCreateView(generics.CreateAPIView):
    """Create a new quote request"""
    queryset = QuoteRequest.objects.all()
    serializer_class = QuoteRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {
                "message": "Thank you for your quote request! I'll review your requirements and send you a detailed proposal within 48 hours.",
                "success": True
            },
            status=status.HTTP_201_CREATED
        )