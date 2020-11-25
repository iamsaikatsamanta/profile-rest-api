from rest_framework.serializers import Serializer
from rest_framework import serializers
class HelloSerializer(Serializer):
    """Serialize Name for testing View"""
    name = serializers.CharField(max_length=10)