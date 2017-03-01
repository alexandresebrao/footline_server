from rest_framework import serializers
from core.models.news import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = News
