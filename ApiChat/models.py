from django.db import models


# Create your models here.

class Chat(models.Model):
    nameSender = models.CharField(max_length=10000)
    sms = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.nameSender)
