from django.shortcuts import render
from rest_framework import generics

from showroom import serializers
from showroom.models import Showroom


class ShowroomList(generics.ListCreateAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer


class ShowroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showroom.objects.all()
    serializer_class = serializers.ShowroomSerializer
