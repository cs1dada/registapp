# _*_ encoding: utf-8 _*_
from django.db import models
from django.contrib.auth.models import User
"""
django.contrib.auth.models.py

class User(models.Model):
username
password
email
first_name
last_name
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __unicode__(self):
        return self.user.username

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()

    def __unicode__(self):
        return "{}({})".format(self.ddate, self.user)
"""
# raw auth
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    def __unicode__(self):
        return self.message
"""