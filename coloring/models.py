from django.db import models

# The Author model has been created for you
class Author(models.Model):
  name = models.CharField(max_length=50)
  lastDrawing = models.CharField(max_length=50, null=True, blank=True)

# Create the Drawing model
class DrawingModel(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  points = models.TextField(null=True)