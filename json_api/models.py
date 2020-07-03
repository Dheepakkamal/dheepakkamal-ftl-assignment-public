from django.db import models
from django.contrib.postgres.fields import JSONField


class User(models.Model):
    user_id = models.CharField(primary_key = True, max_length = 64)
    real_name = models.CharField(max_length = 64, default = "")


class ActivityPeriod(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    time_zone = models.CharField(max_length = 64, default = "")
    activity_period = JSONField(default = dict)
