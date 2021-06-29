from django.forms import ModelForm
from django import forms
from froala_editor.widgets import FroalaEditor

from boardapp.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        labels = {
            'content': '',
            'image': 'thumbnail '
        }
        widgets = {
            'content': FroalaEditor(),
            'image': forms.FileInput(attrs={'class': 'thum',}),
        }