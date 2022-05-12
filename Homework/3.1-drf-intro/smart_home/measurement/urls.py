from django.urls import path
from measurement.views import SensorView, RetrieveSensorView, MeasurementView


urlpatterns = [
   path('sensors/', SensorView.as_view()),
   path('sensors/<int:pk>/', RetrieveSensorView.as_view()),
   path('measurements/', MeasurementView.as_view())
]
