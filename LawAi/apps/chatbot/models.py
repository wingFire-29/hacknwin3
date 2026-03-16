from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    """Model to store chat messages between user and chatbot"""
    ROLE_CHOICES = [
        ('user', 'User'),
        ('bot', 'Chatbot'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.role}: {self.message[:50]}..."
