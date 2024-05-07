from django import forms 
from .models import *

class AddRestoranForm(forms.ModelForm):
    class Meta:
        model = restorans
        fields = ['name', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }
        widgets = {
            'name': forms.TextInput(attrs={ 'style': 'width: 300px;'})
        }


class AddScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['name', 'name_restoran', 'dish_name', 'rating']
