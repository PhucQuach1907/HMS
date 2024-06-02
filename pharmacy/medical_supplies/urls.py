from django.urls import path, include
from rest_framework import routers
from .views import MedicalSuppliesViewSet

router = routers.DefaultRouter()
router.register(r'medical-supplies', MedicalSuppliesViewSet)

urlpatterns = [
    path('', include(router.urls))
]