from django import forms
from board.models import Comment


class CommentForm(forms.ModelForm):
    model = Comment
    fields = ('body',)
    
    
