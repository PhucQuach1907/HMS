from django.urls import path, include
from rest_framework import routers
from .views import PrescriptionViewSet

router = routers.DefaultRouter()
router.register(r'prescription', PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls))
]