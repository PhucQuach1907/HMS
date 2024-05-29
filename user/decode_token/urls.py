from django.urls import path
from .views import decode_token

urlpatterns = [
    path('', decode_token, name='decode_token'),
]