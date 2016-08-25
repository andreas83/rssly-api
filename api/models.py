from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
    	app_label = 'api'
        abstract = True

class Reader(BaseModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.FileField(upload_to='data/avatar')



class RSSSource(BaseModel):
	name = models.CharField( max_length=100 )
	description = models.CharField( max_length=100 )
	image=models.FileField(upload_to='data/src_img/', null=True)
	language = models.CharField( max_length=3 )
	link = models.TextField()

class RSSItem(BaseModel):
	RSSSource = models.ForeignKey(RSSSource, related_name='items', on_delete=models.CASCADE)
	title = models.CharField( max_length=200 )
	description = models.TextField()
	author = models.CharField( max_length=100 )
	link = models.TextField()


class Category(BaseModel):
	ParentCategory = models.ForeignKey('self', blank=False, null=True)
	Reader = models.ManyToManyField(Reader)
	RSSItem = models.ManyToManyField(RSSItem)
	name = models.CharField( max_length=100 )
	slug = models.SlugField(unique=True)
