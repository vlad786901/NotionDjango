from rest_framework import serializers
from .models import Request, RequestMessage


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'title', 'description', 'created_at']


class RequestMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestMessage
        fields = ['id', 'request', 'message', 'created_at']
