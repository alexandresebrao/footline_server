from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from core.models.user import UserAddon
from api.v1.serializers.user import UserSerializer
from django.conf import settings


def getUser(login):
    try:
        return User.objects.get(email=login)
    except:
        try:
            return User.objects.get(username=login)
        except:
            return False
        return False


class AuthenticateView(APIView):
    def get(self, request, *args, **kargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = getUser(username)
        if user:
            user = authenticate(user, password)
            user.get_token()
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        user = User(username=username, password=password, email=email)
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response('', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kargs):
        return Response('')
