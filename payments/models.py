from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.OneToOneField(User)
