from rest_framework import serializers

from showroom.models import Car, Discount, Showroom


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


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "name", "production_brand", "production_country", "production_year"]
