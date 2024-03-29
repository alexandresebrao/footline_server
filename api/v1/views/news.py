from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.v1.serializers.news import NewsSerializer
from core.models.news import News


class NewsAPIView(APIView):
    def get(self, request, page=None, *args, **kargs):
        if request.user.is_authenticated():
            news = News.objects.all()
            serializer = NewsSerializer(news, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kargs):
        if request.user.is_authenticated():
            if request.user.is_staff():
                return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
