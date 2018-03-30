from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TOWNS = (
		('Краснодар', 'Краснодар'),
		('Кропоткин', 'Кропоткин'),
		('Славянск', 'Славянск'),
		('Ростов', 'Ростов'),
		('Шахты', 'Шахты'),
		('Батайск', 'Батайск'),
		('Ставрополь', 'Ставрополь'),
		('Пятигорск', 'Пятигорск'),
		('Кисловодск', 'Кисловодск'),
	)

REGIONS = (
		('Краснодарский Край', 'Краснодарский Край'),
		('Ростовская Область', 'Ростовская Область'),
		('Ставропольский Край', 'Ставропольский Край'),
	)

class Town(models.Model):

	name = models.CharField(max_length=100, choices=TOWNS, default=1, blank=True)
	region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, default=None)

	def __str__(self):
		return '{}'.format(self.name)	

class Region(models.Model):

	name = models.CharField(max_length=100, choices=REGIONS, default=1, blank=True)

	def __str__(self):
		return '{}'.format(self.name)	

class CommentStat(models.Model):
	region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
	town = models.ForeignKey('Town', on_delete=models.SET_NULL, null=True, blank=True)
	comment_num = models.IntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return '{} :: {} :: {}'.format(self.region, self.town, self.comment_num)

class Comment(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
	user_name = models.CharField(max_length=100, null=True)
	user_family_name = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
	town = models.ForeignKey('Town', on_delete=models.SET_NULL, null=True, blank=True)
	patronomic = models.CharField(max_length=100, null=True, blank=True)
	phone = models.CharField(max_length=100, null=True, blank=True)
	comment = models.CharField(max_length=1000, null=False)
	visibility = models.BooleanField(default=True, blank=False)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)	

	def __str__(self):
		return '{} :: {} :: {}'.format(self.comment, self.user_name, self.created_at)					