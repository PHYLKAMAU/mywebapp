from django.db import models

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('web-development', 'Web Development Project'),
        ('mobile-app', 'Mobile App Development'),
        ('cloud-services', 'Cloud & DevOps Services'),
        ('consultation', 'Technical Consultation'),
        ('maintenance', 'Maintenance & Support'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='other')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"


class QuoteRequest(models.Model):
    BUDGET_CHOICES = [
        ('5000-10000', '$5,000 - $10,000'),
        ('10000-25000', '$10,000 - $25,000'),
        ('25000-50000', '$25,000 - $50,000'),
        ('50000+', '$50,000+'),
    ]
    
    TIMELINE_CHOICES = [
        ('asap', 'ASAP'),
        ('1-month', 'Within 1 month'),
        ('2-3-months', '2-3 months'),
        ('3-6-months', '3-6 months'),
        ('flexible', 'Flexible'),
    ]

    SERVICE_CHOICES = [
        ('web-development', 'Web Development'),
        ('mobile-app', 'Mobile App Development'),
        ('cloud-deployment', 'Cloud & Deployment'),
        ('maintenance', 'Maintenance & Support'),
        ('consulting', 'IT Consulting'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES)
    services = models.JSONField(default=list, help_text="List of selected services")
    timeline = models.CharField(max_length=20, choices=TIMELINE_CHOICES)
    description = models.TextField()
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - Quote Request ({self.get_budget_display()})"