from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

class Question(models.Model):
	text = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	score = models.IntegerField()
