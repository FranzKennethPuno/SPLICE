from django import forms
from .models import Profile

class ColorPickerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['color']



