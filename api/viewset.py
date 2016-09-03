
from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer, CategorySerializer, RSSSourceSerializer, RSSItemResourceSerializer
from api.models import RSSItem, RSSSource, Category, RSSItemResource


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RSSItemViewSet(viewsets.ModelViewSet):
	queryset = RSSSource.objects.all()[:5]
	serializer_class = RSSSourceSerializer

	def get_queryset(self):
		queryset = RSSSource.objects.random()
		return queryset

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
