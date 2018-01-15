"""
Posts: each post should have a content and number of likes and belongs to a single user.
"""

from django.conf import settings
from django.db import models
from person.models import Person


# Create your models here.
class BlogPost(models.Model):
	user = models.ForeignKey(Person ,on_delete=models.CASCADE)
	title = models.CharField(max_length=120, null=True, blank=True)
	content = models.TextField(max_length=120, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(null=0, default=0)

	def __str__(self):
		return str(self.user.username)
