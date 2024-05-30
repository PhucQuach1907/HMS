from rest_framework import viewsets

from .models import MedicalRecord
from .serializers import MedicalRecordSerializer


# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
