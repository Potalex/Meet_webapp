from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Activity(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  createdDate = models.DateTimeField(default=timezone.now)
  activateDate = models.DateTimeField(blank=True, null=True)
  
  def publish(self):
    self.activateDate = timezone.now
    self.save()
    
  def __str__(self):
    return self.title