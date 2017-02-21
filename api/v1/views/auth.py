from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from api.v1.serializers.user import UserSerializer
from core.models.register import RegisterToken


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
        token = data.get('token')
        try:
            rt = RegisterToken.objects.get(token=token, use=False)
            userdata = {
                'username': username,
                'password': password,
                'email': email
            }
            user = UserSerializer(data=userdata)
            if user.is_valid():
                user.save()
                rt.use = True
                rt.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(user.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Aki")
            print(data)
            dictionary = {
                'error': {'token': 'token não aceito'}
            }
            return Response(dictionary, status=status.HTTP_400_BAD_REQUEST)


class VerifyToken(APIView):
    def get(self, request, token=None, *args, **kargs):
        try:
            RegisterToken.objects.get(token=token, use=False)

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
