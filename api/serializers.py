from rest_framework import serializers

from django.contrib.auth.models import User
from api.models import RSSItem, RSSSource, Category, RSSItemResource


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class RSSItemResourceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta():
		model = RSSItemResource
		fields = ('id', 'link', 'mime')


class RSSItemSerializer(serializers.HyperlinkedModelSerializer):
	resource = RSSItemResourceSerializer(many=True, read_only=True)

	class Meta():
		model = RSSItem
		fields = ('id', 'title', 'description', 'link', 'resource')


class RSSSourceSerializer(serializers.HyperlinkedModelSerializer):
	items = RSSItemSerializer(many=True, read_only=True)
	class Meta:
		model = RSSSource
		fields = ('id', 'name', 'description', 'image', 'link', 'language', 'items' )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name')
