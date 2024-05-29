import datetime

import jwt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def login(request):
    login_id = request.data.get('login_id')
    password = request.data.get('password')

    print(login_id, password)

    if login_id is None or password is None:
        return Response({'error': 'Vui lòng cung cấp ID và mật khẩu'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, login_id=login_id, password=password)
    if not user:
        return Response({'error': 'ID hoặc mật khẩu không đúng'}, status=status.HTTP_401_UNAUTHORIZED)

    payload = {
        'user_id': user.pk,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response({'token': token}, status=status.HTTP_200_OK)
    return response
