from django import forms
from .models import Topic, Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ["content"]
        widgets = {"content":forms.Textarea()}

class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = ["title", "descripton"]
        widgets = {"title":forms.TextInput(), "descripton":forms.Textarea()}