from django.urls import path
from .views import AirplaneCreateAPIView, AirplaneListApiView

urlpatterns = [
    path('list/', AirplaneListApiView.as_view()),
    path('create', AirplaneCreateAPIView.as_view())
]