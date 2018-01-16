from rest_framework import generics, mixins
from django.http import HttpResponse
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from shared_permissions.permissions import IsOwnerOrReadOnly

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer

	
	def get_queryset(self): 
		return BlogPost.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		self.create(request, *args, **kwargs)


class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return BlogPost.objects.all()


