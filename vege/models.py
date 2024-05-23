from django.db import models

class receipe(models.Model):
    name = models.CharField(max_length=150)
    descp = models.TextField()
    image = models.ImageField(upload_to="reciepe")