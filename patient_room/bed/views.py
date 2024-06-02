from django.shortcuts import render
from rest_framework import viewsets

from .models import Bed
from .serializers import BedSerializer


# Create your views here.
class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
