from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Driver(AbstractUser):
    driver_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    