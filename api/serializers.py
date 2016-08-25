from rest_framework import serializers

from django.contrib.auth.models import User
from api.models import RSSItem, RSSSource


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class RSSItemSerializer(serializers.HyperlinkedModelSerializer):
	items = serializers.StringRelatedField(many=True)
	class Meta:
		model = RSSSource
		fields = ('name', 'description',  'link', 'items')
