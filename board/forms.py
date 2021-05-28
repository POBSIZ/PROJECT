from django import forms
from board.models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': '', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용'
        }
