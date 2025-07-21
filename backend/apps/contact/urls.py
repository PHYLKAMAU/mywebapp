from django.urls import path
from .views import ContactMessageCreateView, QuoteRequestCreateView

urlpatterns = [
    path('message/', ContactMessageCreateView.as_view(), name='contact-message'),
    path('quote/', QuoteRequestCreateView.as_view(), name='quote-request'),
]