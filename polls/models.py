from __future__ import unicode_literals
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
 	def was_published_recently(self):
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Human(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=64)
	height = models.IntegerField(default=0)
	date_of_birth = models.DateTimeField()
	def __str__(self):
		return self.name + " " + self.surname
