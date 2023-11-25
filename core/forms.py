from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    password_delete = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = Thread
        fields = ['title', 'content', 'username','file_uploaded']
       

class PostForm(forms.ModelForm):
    password_delete = forms.CharField(widget=forms.PasswordInput, required=False)
    class Meta:
        model = Post
        fields = ['thread','content', 'username', 'password_delete', 'file_uploaded']