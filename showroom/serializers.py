from rest_framework import serializers

from showroom.models import Car, Discount, Showroom


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ["name", "country", "id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["percentage", "name", "description", "showroom", "cars", "id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["name", "production_brand", "production_country", "production_year", "id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
