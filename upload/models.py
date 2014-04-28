from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Upload(models.Model):
	username = models.CharField(max_length=140)
	upload_file = models.FileField(upload_to='documents/%Y/%m/%d')

