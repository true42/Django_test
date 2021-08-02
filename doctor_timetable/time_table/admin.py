from django.contrib import admin
from .models import Appointment, Timetable


class AppointmentInline(admin.TabularInline):
    model = Appointment


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'from_hour', 'to_hour')
    inlines = [AppointmentInline]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'office', 'day_of_appointment', 'time_of_appointment')
