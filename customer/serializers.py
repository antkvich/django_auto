from rest_framework import serializers

from customer.models import Customer, PurchaseOffer


class PurchaseOfferSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PurchaseOffer
        fields = ["user", "car", "max_price", "id", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Customer
        fields = ["user", "created_at", "updated_at", "balance"]
        read_only_fields = ["user", "created_at", "updated_at", "balance"]
