from django import forms

class PostForm(forms.Form):
    text = forms.CharField(required = True, label = False, max_length = 100 ,widget= forms.TextInput(attrs={'placeholder':'What is in your mind?', 'autocomplete':'off', 'size':'50', 'id': 'text'}))