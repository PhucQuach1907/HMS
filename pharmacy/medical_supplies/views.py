from django.shortcuts import render
from rest_framework import viewsets

from .models import MedicalSupplies
from .serializers import MedicalSuppliesSerializer


# Create your views here.
class MedicalSuppliesViewSet(viewsets.ModelViewSet):
    queryset = MedicalSupplies.objects.all()
    serializer_class = MedicalSuppliesSerializer
