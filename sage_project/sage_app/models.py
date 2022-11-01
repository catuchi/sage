from django.db import models

# Create your models here.

class Room(models.Model):
  # host = None
  # topic = None
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True)  # null=True allows us to create an instance of this class while having this attribute value be null (for the db)
                                                         # blank=True allows us to submit an empty value when submitting a form (for the save method)
  # participants = None
  updated = models.DateTimeField(auto_now=True)          # auto_now takes a timestamp when we save
  created = models.DateTimeField(auto_now_add=True)      # auto_now_add takes a timestamp when we first save or create this instance

  def __str__(self):
    return self.name