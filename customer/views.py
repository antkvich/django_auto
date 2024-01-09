from django.shortcuts import render
from rest_framework import generics

from customer import serializers
from customer.models import Customer, PurchaseOffer
from customer.permissions import IsOwnerOrReadOnly


class PurchaseOfferListView(generics.ListCreateAPIView):
    queryset = PurchaseOffer.objects.all()
    serializer_class = serializers.PurchaseOfferSerializer


class PurchaseOfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PurchaseOffer.objects.all()
    serializer_class = serializers.PurchaseOfferSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
