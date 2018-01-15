from rest_framework import generics, mixins
from ..models import Person
from .serializers import UserSerializer
from shared_permissions.permissions import IsOwnerOrReadOnly

class PersonAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = PersonSerializer

	
	def get_queryset(self): 
		return Person.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		self.create(request, *args, **kwargs)	


class PersonRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = PersonSerializer
	permission_classes = [IsOwnerOrReadOnly]

	def get_queryset(self):
		return User.objects.all()


