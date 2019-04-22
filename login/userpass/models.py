from django.db import models

class User(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):

        return self.title

class Pass(models.Model):

    password = models.CharField(max_length=32)