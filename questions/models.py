from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Question(models.Model):
	text = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	score = models.IntegerField()

	def __str__(self):
		return self.text
