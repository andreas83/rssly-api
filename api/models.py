from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from django.db.models import Count
from random import randint


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'
        abstract = True

class Reader(BaseModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.FileField(upload_to='data/avatar')


class RSS(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index:random_index+10]


class RSSSource(BaseModel):
	name = models.TextField()
	description = models.TextField()
	image=models.FileField(upload_to='data/src_img/', null=True)
	language = models.CharField( max_length=3 )
	link = models.TextField()
	
	objects = RSS()

class RSSItem(BaseModel):
	RSSSource = models.ForeignKey(RSSSource, related_name='items', on_delete=models.CASCADE)
	title = models.TextField()
	description = models.TextField()
	author = models.TextField()
	link = models.TextField()

class RSSItemResource(BaseModel):
	RSSItem = models.ForeignKey(RSSItem, related_name="resource", on_delete=models.CASCADE)
	link = models.TextField()
	mime = models.CharField( max_length=100, null = True )

class Category(BaseModel):
	ParentCategory = models.ForeignKey('self', blank=False, null=True)
	Reader = models.ManyToManyField(Reader)
	RSSItem = models.ManyToManyField(RSSItem, blank=True)
	name = models.CharField( max_length=100 )
	slug = models.SlugField(unique=True)
