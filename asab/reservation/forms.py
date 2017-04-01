from django.forms import ModelForm
from .models import Reservation
from bootstrap3_datetime.widgets import DateTimePicker

class ReservationCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReservationCreateForm, self).__init__(*args, **kwargs)
        self.fields['venue'].widget.attrs.update({'class': 'venue'})
        # self.fields['start_time'].widget.attrs.update({'class': 'start'})
        # self.fields['end_time'].widget.attrs.update({'class': 'end'})

    class Meta:
        model = Reservation
        fields = ('venue','phone', 'start_time', 'end_time')
        widgets = {
            'start_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True}),
            'end_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True})
        }

class ReservationUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['venue'].widget.attrs.update({'class': 'venue'})
        # self.fields['start_time'].widget.attrs.update({'class': 'start'})
        # self.fields['end_time'].widget.attrs.update({'class': 'end'})

    class Meta:
        model = Reservation
        fields = ('venue','phone', 'start_time', 'end_time')
        widgets = {
            'start_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True}),
            'end_time':DateTimePicker(options={"format": "MM/DD/YY HH:mm",
                                                 "sideBySide":True})
        }

