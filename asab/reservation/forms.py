from django.forms import ModelForm
from .models import Reservation, Venue
from bootstrap3_datetime.widgets import DateTimePicker

class ReservationCreateForm(ModelForm):

    def __init__(self, options, *args, **kwargs):
        super(ReservationCreateForm, self).__init__(*args, **kwargs)
        # self.fields['facility'].widget.attrs.update({'class': 'facility'})
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
        fields = ('facility','phone', 'start_time', 'end_time')
        widgets = {
            'start_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True}),
            'end_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True})
        }

