from django.contrib.auth.models import AbstractUser
from djongo import models

class CustomUser(AbstractUser):
    solved_problems = models.JSONField(default=list, blank=True, null=True)
    solving_problems = models.JSONField(default=list, blank=True, null=True)

