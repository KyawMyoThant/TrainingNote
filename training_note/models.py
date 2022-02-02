from ftplib import MAXLINE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Title entity for Training Note and purpose of Training 
# fields are name and Description for easier understanding 
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)

class Title(models.Model):
    title_name = models.CharField(max_length=50, null=False)
    title_description = models.TextField(null=True)
    created_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to="title/images/", blank=True, null=True)

    def __str__(self):
        return self.title_name

class Task(models.Model):
    task_name =  models.CharField(max_length=50, null=False)
    task_description = models.TextField(null=True)
    created_date = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True,blank=True)
    title = models.ForeignKey(Title,related_name='tasks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
        
        