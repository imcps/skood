from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


categories = [
        (1, 'Books'),
        (2, 'Vehicle'),
    ]

# Create your models here.
class Advertisment(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	image = models.FileField()
	price = models.IntegerField()
	category = models.CharField(max_length=100, null=True, blank=True)
	description = models.CharField(max_length=500)
	mobileNumber = models.BigIntegerField()
	address = models.CharField(max_length=150)

	def __str__(self):
		return "%s - %s" % (self.title, self.name)


class Notification(models.Model):
	not_user = models.ForeignKey(User, on_delete=models.CASCADE)
	notification = models.CharField(max_length=800)
	# buy_er = models.CharField(max_length=10000, null=True)
	# product = models.IntegerField(null=True)

	def __str__(self):
		return "%s - %s" % (self.not_user.username, self.notification)



class BlockChain(models.Model):
	log = models.CharField(max_length=8000)		

	def __str__(self):
		return self.log	