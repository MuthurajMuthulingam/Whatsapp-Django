# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.shortcuts import render
from  .models import Message, User, Group
from messaging.serializers import MessageSerializer,UserSerializer, GroupSerializer
# Django API
from django.http import Http404
from rest_framework import generics

# Create your views here.
class MessageList(generics.ListCreateAPIView):
    # setting permiossions
    #authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    # setting permiossions
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class Users(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    # permission
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer