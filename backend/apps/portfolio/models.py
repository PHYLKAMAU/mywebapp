from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('mobile', 'Mobile'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80, help_text="Proficiency percentage (0-100)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="Emoji or icon class", default="🔧")
    description = models.TextField()
    features = models.JSONField(default=list, help_text="List of features as JSON array")
    price_range = models.CharField(max_length=100, blank=True, help_text="e.g., '$5,000 - $10,000'")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.JSONField(default=list, help_text="List of technologies used as JSON array")
    demo_url = models.URLField(blank=True, null=True, help_text="Live demo URL")
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    case_study_url = models.URLField(blank=True, null=True, help_text="Case study URL")
    is_featured = models.BooleanField(default=False)
    completed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-completed_date']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    content = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.client_company}"


class About(models.Model):
    title = models.CharField(max_length=200, default="About Wambui Kamau")
    subtitle = models.CharField(max_length=200, default="Full-Stack Developer & IT Solutions Expert")
    bio = models.TextField(help_text="Your professional bio")
    mission = models.TextField(help_text="Your mission statement")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    years_experience = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    cv_file = models.FileField(upload_to='documents/', blank=True, null=True, help_text="Upload your CV/Resume")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title