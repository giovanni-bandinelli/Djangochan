from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
    
class Thread(Base):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    file_uploaded = models.FileField(upload_to='thread_media', null=True, blank=True)

    #is_pinned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}     {self.title} - {self.created_at}"

class Post(Base):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    file_uploaded = models.FileField(upload_to='reply_media/', null=True, blank=True)
    def __str__(self):
        return f"[{self.thread.title}] {self.created_at} "

    



