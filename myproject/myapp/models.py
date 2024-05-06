from django.db import models

# Create your models here.
class Practice(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

#creating model for blogpost

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30)
    post = models.TextField()
    thumbnail = models.ImageField(upload_to = 'images/', default='')
    def __str__(self):
        return self.title
    
    