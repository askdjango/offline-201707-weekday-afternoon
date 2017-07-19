from django import forms
from .models import Post

# class PostForm(forms.Form):
#   author = forms.CharField()
#   title = forms.CharField()
#   content = forms.CharField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

