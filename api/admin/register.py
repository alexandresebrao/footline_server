from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.user import UserAddon
from core.models.register import RegisterToken
from api.serializers.tokens import RegisterTokenSerializer


class RegisterTokenAPIView(APIView):
    def get(self, request, *args, **kargs):
        data = request.data
        token = data.get('token')
        # try:
        #     user = UserAddon.objects.get(token=token).user
        # except:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        # if user.is_staff():
        tokens = RegisterToken.objects.all()
        serializers = RegisterTokenSerializer(tokens, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kargs):
        data = request.data
        token = data.get('token')
        try:
            user = UserAddon.objects.get(token=token).user
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if user.is_staff():
            re = RegisterToken()
            re.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
