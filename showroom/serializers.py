from rest_framework import serializers

from showroom.models import Showroom


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = [
            "id",
            "name",
            "balance",
            "max_car_year",
            "min_car_year",
            "country",
            "allowed_brands",
            "allowed_countries",
        ]
