from django import forms
from .models import Comment,Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['blogs','name','message']
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment','name','message']