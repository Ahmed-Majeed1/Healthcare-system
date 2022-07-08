from django import forms
from .models import Profile


class ppUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
        
        
class sendform(forms.Form):
    email = forms.EmailField()
    
    def __init__(self):
        return self.email