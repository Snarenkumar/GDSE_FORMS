from django.db import models

# Create your models here.


class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
