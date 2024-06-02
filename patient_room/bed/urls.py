from django.urls import path, include
from rest_framework import routers
from .views import BedViewSet

router = routers.DefaultRouter()
router.register(r'bed-info', BedViewSet)

urlpatterns = [
    path('', include(router.urls))
]