from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('admin', 'Admin'),
    ] 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length = 10, choices= ROLE_CHOICES)

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('cultural', 'Cultural'),
        ('technical', 'Technical'),
        ('sports', 'Sports'),
        ('workshop', 'Workshop'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Club(models.Model):
    CATEGORY_CHOICES = [
        ('cultural', 'Cultural'),
        ('technical', 'Technical'),
        ('sports', 'Sports'),
        ('workshop', 'Workshop'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField() 
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    members_count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    duration = models.IntegerField() 
    instructor = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Registration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registerd_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['student', 'event']

class ClubMembership(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'club']
        
class WorkshopRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'workshop']