from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.nickname  