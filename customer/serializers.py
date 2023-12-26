from rest_framework import serializers

from customer.models import PurchaseOffer


class PurchaseOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOffer
        fields = ["client", "car", "max_price", "color"]
