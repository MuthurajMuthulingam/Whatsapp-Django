# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  .models import Message
from messaging.serializers import MessageSerializer
from messaging.serializers import GroupSerializer
# Django API
from django.http import Http404
from rest_framework import generics

# Create your views here.
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
