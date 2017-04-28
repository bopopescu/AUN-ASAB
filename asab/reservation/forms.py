from django.forms import ModelForm
from .models import Reservation, Venue
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.contrib.auth.models import User

class ReservationCreateForm(ModelForm):

    def __init__(self, options, *args, **kwargs):
        super(ReservationCreateForm, self).__init__(*args, **kwargs)
        # self.fields['facility'].widget.attrs.update({'class': 'facility'})
        if not options:
            options = None
        else:
            self.fields['facility'].choices = options


        # self.fields['start_time'].widget.attrs.update({'class': 'start'})
        # self.fields['end_time'].widget.attrs.update({'class': 'end'})

    class Meta:
        model = Reservation
        fields = ('facility','phone', 'start_time', 'end_time', 'email', 'level','reason')
        widgets = {
            'start_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True}),
            'end_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True})
        }

class ReservationUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['facility'].widget.attrs.update({'class': 'facility'})
        # self.fields['start_time'].widget.attrs.update({'class': 'start'})
        # self.fields['end_time'].widget.attrs.update({'class': 'end'})

    class Meta:
        model = Reservation
        fields = ('facility','phone', 'start_time', 'end_time', 'email', 'level','reason')
        widgets = {
            'start_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True}),
            'end_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True})
        }

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