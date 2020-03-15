from django.db import models

# Create your models here.


class RoomInfo(models.Model):
    RoomID = models.CharField(max_length=30)
    RoomPassword = models.CharField(max_length=30)
    CurFee = models.FloatField(default=0)