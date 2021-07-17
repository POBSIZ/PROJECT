from django.forms import ModelForm
from django import forms
from froala_editor.widgets import FroalaEditor

from boardapp.models import Post, Category


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
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']