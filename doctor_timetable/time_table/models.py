import uuid
from django.db import models


class Timetable(models.Model):
    week_day = models.DateField(blank=True)
    from_hour = models.TimeField(blank=True)
    to_hour = models.TimeField(blank=True)


class Appointment(models.Model):
    date_id = models.ForeignKey(Timetable, on_delete=models.SET_NULL, null=True)
    patient = models.CharField(max_length=100, help_text='Patient Name')
    office = models.CharField(max_length=3, help_text='number office', null=True)
    day_of_appointment = models.DateField()
    time_of_appointment = models.TimeField()

    LOAN_STATUS = (
        ('o', 'On'),
        ('p', 'planned'),
        ('c', 'complete')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='p')

    class Meta:
        ordering = ["time_of_appointment"]

    def __str__(self):
        return f'{self.status}, {self.patient}'


