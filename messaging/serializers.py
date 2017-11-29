from rest_framework import serializers
from messaging.models import Message, Group , LANGUAGE_CHOICES, STYLE_CHOICES

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'time')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name','imageURL')