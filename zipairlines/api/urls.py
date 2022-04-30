from django.urls import path, include

urlpatterns = [
    path('airplane/', include('zipairlines.api.airplane.urls')),
]