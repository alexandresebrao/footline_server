from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.user import UserAddon
from core.models.register import RegisterToken
from api.serializers.tokens import RegisterTokenSerializer
from django.http import Http404


class RegisterTokenAPIView(APIView):
    def get(self, request, token=None, *args, **kargs):
        # try:
        #     user = UserAddon.objects.get(token=token).user
        # except:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        # if user.is_staff()
        if token:
            try:
                tokens = RegisterToken.objects.get(id=token)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializers = RegisterTokenSerializer(tokens, many=True)
        else:
            tokens = RegisterToken.objects.filter(use=False)
            serializers = RegisterTokenSerializer(tokens, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kargs):
        re = RegisterToken()
        re.save()
        return Response(status=status.HTTP_201_CREATED)


class RegisterTokenDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return RegisterToken.objects.get(pk=pk)
        except RegisterToken.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rt = self.get_object(pk)
        serializer = RegisterTokenSerializer(rt)
        return Response(serializer.data)
