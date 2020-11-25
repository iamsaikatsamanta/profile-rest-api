from rest_framework.serializers import Serializer
from rest_framework import serializers
from profile_api import models

class HelloSerializer(Serializer):
    """Serialize Name for testing View"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(validated_data['email'], validated_data['name'],
                                                      validated_data['password'])
        return user

class FeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FeedItem
        fields = ('id', 'user_profile', 'status', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True,
            }
        }