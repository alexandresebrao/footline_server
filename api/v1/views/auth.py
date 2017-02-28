from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from api.v1.serializers.user import UserSerializer
from core.models.register import RegisterToken
from core.models.user import UserAddon
from rest_framework.authtoken.models import Token
import json

def getUser(login):
    try:
        username = User.objects.get(email=login).username
        return username
    except:
        try:
            User.objects.get(username=login)
            return login
        except:
            return False
        return False


class LoginAPI(APIView):
    def get(self, request, *args, **kargs):
        if request.user.is_authenticated():
            user = UserSerializer(request.user)
            return Response(user.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = getUser(username)
        if user:
            user = authenticate(username=user, password=password)
            if user is not None:
                try:
                    UserAddon.objects.get(user=user)
                except:
                    useradd = UserAddon()
                    useradd.user = user
                    useradd.save()
                token, key = Token.objects.get_or_create(user=user)
                return Response(token.key,
                                status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUserAPI(APIView):
    def post(self, request, *args, **kargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        token = data.get('token')
        if getUser(email):
            return Response("{'email': 'Email já cadastrado'}",
                            status=status.HTTP_400_BAD_REQUEST)

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
            dictionary = {
                'error': {'token': 'token não aceito'}
            }
            return Response(json.dumps(dictionary),
                            status=status.HTTP_400_BAD_REQUEST)


class VerifyToken(APIView):
    def get(self, request, token=None, *args, **kargs):
        try:
            RegisterToken.objects.get(token=token, use=False)

            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
