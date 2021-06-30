from django.forms import ModelForm
from django import forms
from froala_editor.widgets import FroalaEditor

from noticeapp.models import Notice


class NoticeCreationForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['content', 'image']
        labels = {
            'content': '',
            'image': 'thumbnail '
        }
        widgets = {
            'content': FroalaEditor(),
            'image': forms.FileInput(attrs={'class': 'thum',}),
        }