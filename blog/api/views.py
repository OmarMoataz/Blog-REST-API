from rest_framework import generics, mixins
from blog.models import Blog
from .serializers import BlogSerializer


class BlogRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field 			= 'pk' # url(?P<pk>\d+)
	serializer_class 		= BlogSerializer		
	
	def get_queryset(self):
		return Blog.objects.all()


class BlogAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BlogSerializer

	
	def get_queryset(self): 
		return Blog.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		self.create(request, *args, **kwargs)	