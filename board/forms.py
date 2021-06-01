from django import forms
from board.models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.CharField(
                # attrs={'class': '', 'style': 'width: 100%'},
                widget=CKEditorUploadingWidget()
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용'
        }
