from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Timetable


class AppointmentDate(forms.Form):
    appointment_date = forms.DateField(help_text='enter date')

    def clean_appointment_date(self):
        data = self.cleaned_data['appointment_date']

        if data < Timetable.week_day:
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > Timetable.week_day:
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
