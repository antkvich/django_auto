from django.shortcuts import render
from rest_framework import generics

from showroom import serializers
from showroom.models import Car, Discount, Showroom


class ShowroomList(generics.ListCreateAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class ShowroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


class DiscountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
