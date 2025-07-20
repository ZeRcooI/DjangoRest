from django.shortcuts import render
from rest_framework import generics
from women.models import Women
from women.serializers import WomenSerializers


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
