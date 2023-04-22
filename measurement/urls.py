from django.urls import path
from measurement.views import SensorView, SensorOne, Measurement

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorOne.as_view()),
    path('measurements/', Measurement.as_view())
]
