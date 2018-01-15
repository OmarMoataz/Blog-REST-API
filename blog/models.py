from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=20, null=True, blank=True)
	description = models.TextField(max_length=280, null=True, blank=True)

	def __str__(self):
		return str(self.title)


