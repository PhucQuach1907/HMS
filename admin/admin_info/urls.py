from django.urls import path, include
from rest_framework import routers
from .views import AdminViewSet

router = routers.DefaultRouter()
router.register(r'admin', AdminViewSet)

urlpatterns = [
    path('', include(router.urls))
]