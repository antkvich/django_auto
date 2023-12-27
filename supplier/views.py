from django.shortcuts import render
from rest_framework import generics

from supplier import serializers
from supplier.models import Supplier


class SupplierListView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
