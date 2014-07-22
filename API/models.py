__author__ = 'albertlwohletz'
from django.db import models

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class Spaces(models.Model):
    name = models.CharField(max_length=200)

class Access(models.Model):
    user = models.ForeignKey('AuthUser')
    space = models.ForeignKey('Spaces')
    access_type = models.CharField(max_length=200)

class Pending(models.Model):
    user = models.ForeignKey('AuthUser')
    space = models.ForeignKey('Spaces')
    access_type = models.CharField(max_length=200)
    explanation_string = models.CharField(max_length=200)

