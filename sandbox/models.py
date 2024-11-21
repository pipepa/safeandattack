
from django.db import models

class VulnerableUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Навмисно не хешується

    def __str__(self):
        return self.username