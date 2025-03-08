from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FitLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True , blank=True)
    height = models.FloatField(null=True , blank=True)
    date = models.DateTimeField(auto_now_add=True)
