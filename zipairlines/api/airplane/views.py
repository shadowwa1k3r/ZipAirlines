from rest_framework.generics import CreateAPIView, ListAPIView
from zipairlines.models.airplane import Airplane
from .serializers import AirplaneCreateSerializer, AirplaneListDetailSerializer


class AirplaneCreateAPIView(CreateAPIView):
    serializer_class = AirplaneCreateSerializer
    queryset = Airplane.objects.all()


class AirplaneListApiView(ListAPIView):
    serializer_class = AirplaneListDetailSerializer
    
    def def get_queryset(self):
        qs = Airplane.objects.all()
        airplane_id = self.request.GET.get('airplane_id')
        if airplane_id:
            qs = qs.filter(airplane_id=airplane_id)

        return queryset
