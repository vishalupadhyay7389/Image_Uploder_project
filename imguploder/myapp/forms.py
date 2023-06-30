from django import forms
from .models import Images

class Imageforms(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        labels = {'photos':''}