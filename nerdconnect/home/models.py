from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=60000)
    created_at = models.DateTimeField(auto_now_add=True)


class DateRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requests = models.IntegerField(default=1)


class Dates(models.Model):
    sender = models.ForeignKey(
        User, related_name="sent_requests", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User, related_name="_requests", on_delete=models.CASCADE
    )
    request_date = models.DateTimeField(auto_now_add=True)
