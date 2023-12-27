from django.shortcuts import render
from rest_framework import generics

from showroom import serializers
from showroom.models import Car, Discount, Showroom


class ShowroomListView(generics.ListCreateAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class ShowroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class DiscountListView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


class CarListView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
