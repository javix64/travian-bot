from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MaterialsSerializer, TroopsSerializer
from .models import Materials, Troops

class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all().order_by('name')
    serializer_class = MaterialsSerializer

class TroopsViewSet(viewsets.ModelViewSet):
    queryset = Troops.objects.all().order_by('name')
    serializer_class = TroopsSerializer