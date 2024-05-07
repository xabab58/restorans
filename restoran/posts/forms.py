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
        labels = {
            'name': 'Имя',
            'name_restoran': 'Название ресторана',
            'dish_name': 'Название блюда',
            'rating': 'Рейтинг',
        }
    
    def __init__(self, *args, **rwargs):
        super(AddScoreForm, self).__init__(*args, **rwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name_restoran'].widget.attrs['class'] = 'form-control'
        self.fields['dish_name'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['class'] = 'form-control'

        