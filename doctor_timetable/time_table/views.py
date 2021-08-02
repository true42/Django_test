from django.shortcuts import render
from rest_framework import viewsets
from .models import Timetable
from .serializers import TimetableSerialezer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all().order_by('week_day')
    serializer_class = TimetableSerialezer