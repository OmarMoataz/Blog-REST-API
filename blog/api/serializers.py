from rest_framework import serializers

from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = [	
			'pk',
			'title',
			'description',
		]


	def validate_title(self, value):
		#This is to check whether a blog title is unique.
		qs = Blog.objects.filter(title__iexact=value)
		#Excluding current instance from query set.
		if self.instance:
			qs = qs.exclude(pk=self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError("The title must be unique")
		return value