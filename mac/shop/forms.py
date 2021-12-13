from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class demo(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='pass')


    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']


# class
# def clean(self):
#     cleaned_data = super().clean()
#     valpwd = self.clean_data['password']
#     valrpwd = self.clean_data['rpassword']
#     if valpwd != valrpwd:
#         raise forms.ValidationError('Password does not match')