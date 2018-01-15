"""
Users: each user should have a unique username, unique email and password.
"""
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(User):
	class Meta:
		proxy = True

	def __str__(self):
		return str(self.username)




