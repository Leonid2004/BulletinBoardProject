from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=3500)
    whoLiked = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="whoLiked")
    Likes = models.IntegerField(default=0,)
    whoDisliked = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="whoDisliked")
    Dislikes = models.IntegerField(default=0)
    Category = models.CharField(max_length=20, default="Общее")
    filesForWeb = models.ImageField(upload_to='images/',default="",blank=True)



class Messages(models.Model):
    text = models.CharField(max_length=1500)
    msgTo = models.OneToOneField(User,related_name="toPerson",on_delete=models.CASCADE,)
    msgFrom = models.OneToOneField(User,related_name="fromPerson",on_delete=models.CASCADE,)

