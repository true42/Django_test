from rest_framework import serializers
from .models import Timetable, Appointment


class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    appointment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Timetable
        fields = ('week_day', 'from_hour', 'to_hour', 'appointment')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('status', 'patient', 'office', 'time_of_appointment')
