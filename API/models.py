__author__ = 'albertlwohletz'
from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)

class Spaces(models.Model):
    name = models.CharField(max_length=200)

class Access(models.Model):
    user_id = models.ForeignKey('Users')
    space_id = models.ForeignKey('Spaces')
    access_type = models.CharField(max_length=200)

class Pending(models.Model):
    user_id = models.ForeignKey('Users')
    space_id = models.ForeignKey('Spaces')
    access_type = models.CharField(max_length=200)
    explanation_string = models.CharField(max_length=200)
