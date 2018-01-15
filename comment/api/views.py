from rest_framework import generics, mixins
from .serializers import CommentSerializer
from shared_permissions.permissions import IsOwnerOrReadOnly

class CommentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = CommentSerializer

	
	def get_queryset(self): 
		return Comment.objects.all()

	def perform_create(self, serializer):
		serializer.save(content=self.request.content)

	def post(self, request, *args, **kwargs):
		self.create(request, *args, **kwargs)	


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = CommentSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return Comment.objects.all()


