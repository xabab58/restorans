from django import forms 
from .models import *

class AddRestoranForm(forms.ModelForm):
    class Meta:
        model = restorans
        fields = ['name', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }
