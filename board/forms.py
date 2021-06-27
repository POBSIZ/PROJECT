from django import forms
from board.models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from froala_editor.widgets import FroalaEditor

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=FroalaEditor)
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': '',
        }
        # widgets = {
        #     'content': forms.CharField(
        #         # attrs={'class': '', 'style': 'width: 100%'},
        #         widget=CKEditorUploadingWidget()
        #     ),
        # }
        widgets = {
            'content': FroalaEditor()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용'
        }
