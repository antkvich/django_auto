from django.shortcuts import render
from rest_framework import generics

from customer import serializers
from customer.models import PurchaseOffer


class PurchaseOfferList(generics.ListCreateAPIView):
    queryset = PurchaseOffer.objects.all()
    serializer_class = serializers.PurchaseOfferSerializer


class PurchaseOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOffer.objects.all()
    serializer_class = serializers.PurchaseOfferSerializer
