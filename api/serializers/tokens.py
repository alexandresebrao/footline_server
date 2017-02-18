from core.models.register import RegisterToken
from rest_framework import serializers


class RegisterTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterToken
        fields = ('token', 'use')
