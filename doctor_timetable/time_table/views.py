from django.shortcuts import render
from rest_framework import viewsets
from .models import Timetable, Appointment
from .serializers import TimetableSerializer, AppointmentSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all().order_by('week_day')
    serializer_class = TimetableSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
