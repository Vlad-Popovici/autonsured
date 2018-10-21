from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title     = models.CharField(max_length=150)
	slug      = models.SlugField()
	body      = models.TextField(blank=True)
	image     = models.ImageField(null=True,blank=True)
	#Need to add a date field thats automatically added as date.now() when publishing

	def __str__(self):
		return self.title