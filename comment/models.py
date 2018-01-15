from django.db import models

# Create your models here.

"""
Comments: each comment should have a content and a number of likes and belongs to a single post.
"""

from django.db import models
from person.models import Person
from postings.models import BlogPost


# Create your models here.
class Comment(models.Model):
	user = models.ForeignKey(Person, on_delete=models.CASCADE)
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	content = models.TextField(max_length=280, null=True, blank=True)
	

	def __str__(self):
		return str(self.content)


