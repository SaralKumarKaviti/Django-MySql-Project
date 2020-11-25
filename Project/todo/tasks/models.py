from django.db import models

# Create your models here.

class Register(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	email = models.CharField(max_length=50)
	phoneNumber = models.CharField(max_length=50) 
	profilePic = models.ImageField(upload_to='images/',default='')
	createdOn=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.firstName


class Task(models.Model):
	name=models.CharField(max_length=200)
	complete=models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


