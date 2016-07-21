from django.db import models

# Create your models here.
class Region(models.Model):
	region_id = models.BigIntegerField(primary_key = True)
	region_name = models.TextField(max_length=50)

class Client(models.Model):
	client_id = models.BigIntegerField(primary_key = True)
	company_name = models.TextField(max_length=50)
	regions = models.ManyToManyField(Region)

class Provider(models.Model):
	provider_id = models.BigIntegerField(primary_key = True)
	company_name = models.TextField(max_length=50)
	regions = models.ManyToManyField(Region)
		
		
		