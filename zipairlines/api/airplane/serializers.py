from rest_framework import serializers
from zipairlines.models.airplane import Airplane

class AirplaneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = (
            'airplane_id',
            'passenger_count',
        )


class AirplaneListDetailSerializer(serializers.ModelSerializer):
    fuel_consumption_per_minute = serializers.SerializerMethodField()
    flight_time = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = (
            'airplane_id',
            'passenger_count',
            'fuel_consumption_per_minute'
            'flight_time'
        )

    def get_fuel_consumption_per_minute(self, obj):
        return obj.fuel_consumption_per_minute

    def get_flight_time(self, obj):
        return obj.flight_time
