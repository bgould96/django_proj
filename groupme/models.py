from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Camp(models.Model):
    camp_id = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=200)

    def __str__(self):
        return self.camp_name

class User(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE, default=1)
    user_id = models.CharField(max_length=200, default="")
    user_name = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=200, default="")
    user_friendly_name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.user_friendly_name

class Group(models.Model):
    group_id = models.CharField(max_length=200, default="")
    group_name = models.CharField(max_length=200, default="")
    tracked = models.BooleanField(default=False)

    def __str__(self):
        return self.group_name

class Bot(models.Model):
    bot_name = models.CharField(max_length=200, default="")
    bot_id = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.bot_name

class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender_id = models.CharField(max_length=200, default="")
    message_id = models.CharField(max_length=200, default="")
    message_text = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.message_text

class Favorite(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.user_id

class Access_Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.token