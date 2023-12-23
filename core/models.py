from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    idcookie = models.CharField(max_length=36)  # "Track" the actual user by cookie
    username = models.CharField(max_length=15, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file_uploaded = models.FileField(upload_to='post_media/', null=True, blank=True)
    thread = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"[{self.id}] {self.created_at}"

