from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Channel(models.Model):
	name = models.CharField(max_length=300)
	creator = models.ForeignKey(User,on_delete=models.CASCADE)
	subscribers = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Video(models.Model):
	name = models.CharField(max_length=400)
	description = models.TextField()
	channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
	videolink = models.CharField(max_length=300)

	def __str__(self):
		return self.name