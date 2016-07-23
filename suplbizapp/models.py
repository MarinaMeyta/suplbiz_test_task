from django.db import models

# Create your models here.
class Region(models.Model):
	region_id = models.AutoField(primary_key = True)
	region_name = models.TextField(max_length=50)

	def __unicode__(self):
		return u'%s %s' % (self.region_id, self.region_name)

class Client(models.Model):
	client_id = models.AutoField(primary_key = True)
	c_company_name = models.TextField(max_length=50)
	c_regions = models.ManyToManyField(Region)

	def __unicode__(self):
		return u'%s %s' % (self.client_id, self.c_company_name)

class Provider(models.Model):
	provider_id = models.AutoField(primary_key = True)
	p_company_name = models.TextField(max_length=50)
	p_regions = models.ManyToManyField(Region)

	def __unicode__(self):
		return u'%s %s' % (self.provider_id, self.p_company_name)
		
		
		