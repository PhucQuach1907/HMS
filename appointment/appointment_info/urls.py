from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'appointment', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]