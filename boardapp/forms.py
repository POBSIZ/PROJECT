from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor

from boardapp.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'content', 'image']
        labels = {
            'content': '',
        }
        widgets = {
            'content': FroalaEditor()
        }