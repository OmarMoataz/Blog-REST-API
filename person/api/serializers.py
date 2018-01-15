from rest_framework import serializers
from models import Person


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = [
			'pk',
			'username',
			'email',
		]
		read_only_fields = ['user']

