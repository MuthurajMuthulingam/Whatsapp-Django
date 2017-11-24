# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length= 100)
    time = models.TimeField(auto_now=True)

class User(models.Model):
    name = models.CharField(max_length= 100)
    number = models.CharField(max_length= 15)
    statusMessage = models.CharField(max_length= 200)
    imageURL = models.URLField(max_length= 200)


class Group(models.Model):
    name = models.CharField(max_length= 200)
    imageURL = models.URLField(max_length= 200)