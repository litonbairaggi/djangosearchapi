from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64, blank=True, default='')
    email = models.EmailField(max_length=64, blank=True, default='', unique=True)
    subject = models.CharField(max_length=64, blank=True, default='')
    text = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.name
    
