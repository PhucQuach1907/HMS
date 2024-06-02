from django.urls import path, include
from rest_framework import routers
from .views import MedicationViewSet

router = routers.DefaultRouter()
router.register(r'medication', MedicationViewSet)

urlpatterns = [
    path('', include(router.urls))
]