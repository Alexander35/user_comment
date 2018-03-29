from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TOWNS = (
		(1, 'Краснодар'),
		(2, 'Кропоткин'),
		(3, 'Славянск'),
		(4, 'Ростов'),
		(5, 'Шахты'),
		(6, 'Батайск'),
		(7, 'Ставрополь'),
		(8, 'Пятигорск'),
		(9, 'Кисловодск'),
	)

REGIONS = (
		(1, 'Краснодарский Край'),
		(2, 'Ростовская Область'),
		(3, 'Ставропольский Край'),
	)

class Town(models.Model):

	name = models.CharField(max_length=100, choices=TOWNS, default=1, blank=True)

	def __str__(self):
		return '{}'.format(self.name)	

class Region(models.Model):

	name = models.CharField(max_length=100, choices=REGIONS, default=1, blank=True)

	def __str__(self):
		return '{}'.format(self.name)	

class Comment(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
	region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
	town = models.ForeignKey('Town', on_delete=models.SET_NULL, null=True, blank=True)
	patronomic = models.CharField(max_length=100, null=True, blank=True)
	tel = models.CharField(max_length=100, null=True, blank=True)
	comment = models.CharField(max_length=1000, null=False)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)	

	def __str__(self):
		return '{}'.format(self.name)					