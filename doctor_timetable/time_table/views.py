from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Timetable, Appointment
from .serializers import TimetableSerializer, AppointmentSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Timetable.objects.all().order_by('week_day')
    serializer_class = TimetableSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
