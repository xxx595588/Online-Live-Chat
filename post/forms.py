from django import forms

class ChatRoomForm(forms.Form):
    name = forms.CharField(required = True, label = 'Name of the room', max_length = 100 ,widget= forms.TextInput(attrs={'placeholder':'Enter existed chat room name or create a new one!', 'autocomplete':'off'}))

class PostForm(forms.Form):
    text = forms.CharField(required = True, label = False, max_length = 100 ,widget= forms.TextInput(attrs={'placeholder':'What is in your mind?', 'autocomplete':'off', 'size':'50', 'id': 'text'}))
    room = forms.CharField(widget = forms.HiddenInput(attrs={'id': 'room'}))