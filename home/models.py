from django.db import models

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


