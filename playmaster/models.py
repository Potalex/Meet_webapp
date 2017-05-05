from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Activity(models.Model):
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  createdDate = models.DateTimeField(default=timezone.now)
  activateDate = models.DateTimeField(blank=True, null=True,default=timezone.now)
  content = models.TextField(blank = True, null = True) 
  
  def publish(self):
    self.createdDate = timezone.now
    self.save()
    
  def __str__(self):
    return self.title
    
class MsgPost(models.Model):
    user = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-datetime']
        
class MsgPostAdmin(admin.ModelAdmin):
    list_display = ('title','datetime','user')
    
admin.site.register(MsgPost, MsgPostAdmin)