from django.db import models
from django.contrib.auth.models import User

class receipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=150)
    descp=models.TextField()
    image=models.ImageField(upload_to="reciepe")