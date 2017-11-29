from rest_framework import serializers
from messaging.models import Message, Group , LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Message
        fields = ('id', 'message', 'time','owner')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name','imageURL')

class UserSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True,queryset=Message.objects.all())
    class Meta:
        model = User
        fields = ('id','username','name','number','statusMessage','imageURL','messages')