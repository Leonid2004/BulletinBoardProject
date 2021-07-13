from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=3500)
    whoLiked = models.ForeignKey(User,on_delete=models.CASCADE,)
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)
    filesForWeb = models.ImageField(upload_to='images/',default="")

class Messages(models.Model):
    text = models.CharField(max_length=1500)
    msgTo = models.OneToOneField(User,related_name="toPerson",on_delete=models.CASCADE,)
    msgFrom = models.OneToOneField(User,related_name="fromPerson",on_delete=models.CASCADE,)

