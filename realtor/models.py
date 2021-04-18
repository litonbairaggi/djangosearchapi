from django.db import models
from datetime import datetime

# Create your models here.
class Agent(models.Model):
    name=models.CharField(max_length=64, blank=False)
    biodata=models.TextField(max_length=100, blank=False)
    email=models.EmailField(max_length=64, blank=False, unique=False)
    phone=models.CharField(max_length=17, blank=False, unique=True)
    image=models.ImageField(upload_to='realtor/', blank=False)
    top_seller=models.BooleanField(default=False)
    date_hired=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name