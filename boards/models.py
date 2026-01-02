from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    name= models.CharField(max_length=50,unique=True)
    discription= models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject= models.CharField(max_length=300)
    board= models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by= models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

class Post (models.Model):
    message = models.CharField(max_length=4000 )
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
