from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="pics/",null=True)
	age=models.IntegerField()
	uniqueid=models.CharField(max_length=6)