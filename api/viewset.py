
from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer, RSSItemSerializer
from api.models import RSSItem, RSSSource


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RSSItemViewSet(viewsets.ModelViewSet):
	queryset = RSSSource.objects.all()
	serializer_class = RSSItemSerializer