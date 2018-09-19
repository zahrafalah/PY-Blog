from django import forms

from .models import posts

class PostForm(forms.ModelForm):
   class Meta:
       model = posts
       fields = [
           'title',
           'author',
           'bodytext',
           'timestamp'
       ]

#Form is not a model form. it is just a standard django form, that we need to declare our inputs
class RawPostForm(forms.Form):    
    author = forms.CharField(max_length = 30) 
    title = forms.CharField(max_length=100) 
    bodytext = forms.CharField()
  

    