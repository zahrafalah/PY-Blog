from django.db import models

# Create your models here.
# create a table by creating a class.
class posts (models.Model):

  #variable fields
  author = models.CharField(max_length = 30) 
  title = models.CharField(max_length=100) 
  bodytext = models.TextField(blank=True, null=True)
  timestamp = models.DateTimeField(blank=True, null=True)
  featured = models.BooleanField(default=False)