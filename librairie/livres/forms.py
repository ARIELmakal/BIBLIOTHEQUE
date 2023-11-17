
from django import forms
from .models import Messages

class Forms(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('nom', 'email', 'message')
