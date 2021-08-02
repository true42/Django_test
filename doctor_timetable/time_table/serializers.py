from rest_framework import serializers

from .models import Timetable, Appointment


class TimetableSerialezer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Timetable
        fields = ('week_day', 'from_hour', 'to_hour')
