import datetime
from rest_framework import serializers
from .models import Timetable, Appointment


def add_delta(tme, delta):
    return (datetime.datetime.combine(datetime.date.today(), tme) +
            delta).time()


class TimetableSerializer(serializers.ModelSerializer):
    appointment = serializers.StringRelatedField(many=True)

    class Meta:
        model = Timetable
        fields = ('week_day', 'from_hour', 'to_hour', 'appointment')


class AppointmentSerializer(serializers.ModelSerializer):
    time_of_appointment = serializers.TimeField()
    day_of_appointment = serializers.DateField()

    def validate(self, data):
        appoint_time = data['time_of_appointment']
        appoint_date = data['day_of_appointment']
        appoint_long = 20
        tt = (Timetable.objects
              .filter(week_day__exact=appoint_date)
              .filter(from_hour__lte=appoint_time, to_hour__gt=add_delta(appoint_time, datetime.timedelta(minutes=appoint_long)))
              )
        if len(tt) == 0:
            raise serializers.ValidationError('Not found free time to appointment')
        if len(tt) > 1:
            raise serializers.ValidationError('Error: To many Timetable')

        return super().validate(data)

    class Meta:
        model = Appointment
        fields = ('status', 'patient', 'office', 'day_of_appointment', 'time_of_appointment')
