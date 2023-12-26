from django.shortcuts import render
from rest_framework import generics

from supplier import serializers
from supplier.models import Supplier


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
