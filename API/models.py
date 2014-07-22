__author__ = 'albertlwohletz'
from django.db import models
from django.contrib.auth.models import User


class Spaces(models.Model):
    name = models.CharField(max_length=200)

class Access(models.Model):
    user = models.ForeignKey(User)
    space = models.ForeignKey(Spaces)
    access_type = models.CharField(max_length=200)

class Pending(models.Model):
    user = models.ForeignKey(User)
    space = models.ForeignKey(Spaces)
    access_type = models.CharField(max_length=200)
    explanation_string = models.CharField(max_length=200)
