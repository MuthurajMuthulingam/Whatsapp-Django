# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Authontication

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

#authontication process
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        #Token.objects.create(user=instance)
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length= 100)
    time = models.TimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='Message', on_delete=models.CASCADE)
    class Meta:
        ordering = ('time',)

class User(models.Model):
    name = models.CharField(max_length= 100)
    number = models.CharField(max_length= 15)
    statusMessage = models.CharField(max_length= 200)
    imageURL = models.URLField()
    message = models.ForeignKey(Message,on_delete=models.CASCADE) # One to Many relation between User and Messages
    group = models.ManyToManyField("Group") # Many to Many relations between User and group
    class Meta:
        ordering = ('name',)

class Group(models.Model):
    name = models.CharField(max_length= 200)
    imageURL = models.URLField(max_length= 200)
    users = models.ManyToManyField("User",related_name="users")
    class Meta:
        ordering = ('name',)