from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class tempatParkir(models.Model):

	STATUS_CHOICES = (
		("kosong","Kosong"),
		("booking","Booking"),
	)
	id_parkir = models.CharField(max_length=5,primary_key=True)
	status = models.CharField(
		choices=STATUS_CHOICES,
		max_length=50,default='kosong')
	position = models.IntegerField(null=False)
	position1 = models.IntegerField(null=False)
	delayposition = models.IntegerField(null=False)
	delayposition1 = models.IntegerField(null=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return "{}.{}".format(self.id,self.id_parkir)
	