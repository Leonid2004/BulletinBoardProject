from django import forms
from .models import Post
import request


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text','Category','filesForWeb']