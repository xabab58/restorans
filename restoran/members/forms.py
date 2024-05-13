from django.contrib.auth.forms import  UserCreationForm
# from django.contrib.auth.models import User 
from django import forms

from .models import User


class RegisterUserForm(UserCreationForm):
    last_name = forms.CharField(max_length=50, label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    patronymic = forms.CharField(max_length=50, label='Отчество', widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'patronymic', 'password1', 'password2' )


    def __init__(self, *args, **rwargs):
        super(RegisterUserForm, self).__init__(*args, **rwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'