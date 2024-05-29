import jwt
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user_info.models import User
from user_info.serializers import UserSerializer


# Create your views here.
@api_view(['GET'])
def decode_token(request):
    token = request.headers.get('Authorization')
    if not token:
        return Response({'error': 'Vui lòng đăng nhập!'}, status=status.HTTP_401_UNAUTHORIZED)

    token = token.split('Bearer ')[1] if token.startswith('Bearer ') else None
    try:
        decoded_payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = decoded_payload['user_id']
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token hết hạn, vui lòng đăng nhập lại.'}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({'error': 'Token không hợp lệ, vui lòng đăng nhập lại.'}, status=status.HTTP_401_UNAUTHORIZED)
