from django.db import models
from utils.models import Timestamp


class Customer(Timestamp):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name
