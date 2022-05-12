from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'sensor', 'temperature')