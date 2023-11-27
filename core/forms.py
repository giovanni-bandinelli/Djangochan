from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    password_delete = forms.CharField(widget=forms.PasswordInput, required=False)#actually useless rn

    class Meta:
        model = Thread
        fields = ['title', 'content', 'username', 'file_uploaded']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title.strip():
            raise forms.ValidationError("'Title' is a required field to create a new thread.")
        return title

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.strip():
            username = "Anonymous"
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers.")
        return username

    def clean_content(self):
        content = self.cleaned_data['content']
        content_length = len(content)
        if content_length > 2000:
            raise forms.ValidationError(f"Your comment is too long. Please keep it under 2000 characters. (currently {content_length})")
        return content

    def clean_file_uploaded(self):
        file_uploaded = self.cleaned_data['file_uploaded']
        if not file_uploaded:
            raise forms.ValidationError("It's necessary to add an image to start a new thread.")
        if file_uploaded and file_uploaded.size > 10 * 1024 * 1024:
            raise forms.ValidationError("File size should not exceed 10 MB.")
        return file_uploaded


class PostForm(forms.ModelForm):
    password_delete = forms.CharField(widget=forms.PasswordInput, required=False)#actually useless rn

    class Meta:
        model = Post
        fields = ['content', 'username', 'file_uploaded']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.strip():
            username = "Anonymous"
        if not username.isalnum():
            raise forms.ValidationError("Username can only contain letters and numbers.")
        return username

    def clean_content(self):
        content = self.cleaned_data['content']
        content_length = len(content)
        if not content.strip():
            raise forms.ValidationError("A reply can't have an empty comment")
        if content_length > 2000:
            raise forms.ValidationError(f"Your comment is too long. Please keep it under 2000 characters. (currently {content_length})")
        return content

    def clean_file_uploaded(self):
        file_uploaded = self.cleaned_data['file_uploaded']
        if file_uploaded and file_uploaded.size > 10 * 1024 * 1024:
            raise forms.ValidationError("File size should not exceed 10 MB.")
        return file_uploaded
