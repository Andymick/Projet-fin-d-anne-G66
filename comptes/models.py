from django.db import models

class Utilisateur(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)