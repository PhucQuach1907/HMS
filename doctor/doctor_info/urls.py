from django.urls import path, include
from rest_framework import routers
from .views import DoctorViewSet

router = routers.DefaultRouter()
router.register(r'doctor', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls))
]