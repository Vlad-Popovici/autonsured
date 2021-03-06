from django.db import models
from blog.models import BlogPost

# Create your models here.
class Comment(models.Model):
    name    = models.CharField(max_length=100)
    body    = models.TextField(blank=True,null=True)
    title   = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    
    def __str__(self):
        return "Comment from: " + self.name
    
    class Meta:
        ordering = ('name',)
        
        

class Company(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    company  = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name