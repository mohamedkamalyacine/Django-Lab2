from django import forms
from polls.models import Question

class PostForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','content']