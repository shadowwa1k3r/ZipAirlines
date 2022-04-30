from django.urls import path
from .views import AirplaneCreateAPIView, AirplaneListApiView

urlpatterns = [
    path('list/', AirplaneListApiView.as_view(), name='get_all_airplanes'),
    path('create', AirplaneCreateAPIView.as_view(), name='create_airplane')
]