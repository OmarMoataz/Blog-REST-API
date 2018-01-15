"""
Blogs: each blog must have a unique title, a description and a list of users.
"""

from django.db import models
from person.models import Person

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=20, null=True, blank=True)
	description = models.TextField(max_length=280, null=True, blank=True)
	user = models.ManyToManyField(Person)

	def __str__(self):
		return str(self.title)


