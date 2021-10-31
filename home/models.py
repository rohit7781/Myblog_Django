from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Contact(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.EmailField()
    queries = models.TextField()
    #to view name in admin window
    def __str__(self):
        return self.first + " "+self.last

class requestblog(models.Model):
    topic = models.CharField(max_length=50)
    desc = models.TextField()
    def __str__(self) :
        return self.topic

#creating a Blog template
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

