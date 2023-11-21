from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, default='anonymous')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file_uploaded = models.FileField(upload_to='thread_media', null=True, blank=True)
    #is_pinned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} - {self.created_at}"

  
class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, default='anonymous')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file_uploaded = models.FileField(upload_to='post_media/', null=True, blank=True)
   # is_op = models.BooleanField(default=False)
    def __str__(self):
        return f"[{self.thread.title}] {self.created_at} "

    



