from django.db import models

class Funcionario(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)