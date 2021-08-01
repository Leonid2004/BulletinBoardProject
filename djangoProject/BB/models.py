from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
POSITIONS = [
    ("Танки", 'Танки'),
    ("Хиллы", 'Хиллы'),
    ("ДД", 'ДД'),
    ("Торговцы", 'Торговцы'),
    ("Гилдмастеры", 'Гилдмастеры'),
    ("Квестгиверы", 'Квестгиверы'),
    ("Кузнецы", 'Кузнецы'),
    ("Кожевники", 'Кожевники'),
    ("Зельевары", 'Зельевары'),
    ("Мастера заклинаний", 'Мастера заклинаний'),
]
class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True, unique=False)
    title = models.CharField(max_length = 75)
    text = models.CharField(max_length=3500)
    whoLiked = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="whoLiked")
    Likes = models.IntegerField(default=0,)
    whoDisliked = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,related_name="whoDisliked")
    Dislikes = models.IntegerField(default=0)
    Category = models.CharField(max_length=20, choices=POSITIONS)
    filesForWeb = models.ImageField(upload_to='images/',default="",blank=True)



class Messages(models.Model):
    text = models.CharField(max_length=1500)
    msgTo = models.OneToOneField(User,related_name="toPerson",on_delete=models.CASCADE,)
    msgFrom = models.OneToOneField(User,related_name="fromPerson",on_delete=models.CASCADE,)

