from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'email',]


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        email_ending = 'aun.edu.ng'

        if email_ending not in cd['email']:
            raise forms.ValidationError('You need a valid AUN mail to register')

        return cd['email']
