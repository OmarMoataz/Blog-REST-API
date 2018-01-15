from rest_framework import generics
from blog.models import Blog
from .serializers import BlogSerializer


class BlogRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field 			= 'pk' # url(?P<pk>\d+)
	serializer_class 		= BlogSerializer		
	
	def get_queryset(self):
		return Blog.objects.all()

