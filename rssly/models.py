from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(models.Model):
	name =models.CharField(max_length=100, primary_key=True)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	avatar = models.FileField(upload_to='data/avatar')

class Category(models.Model):
	parent_cat = models.ForeignKey('self', blank=False, null=True)
	name = models.CharField( max_length=100 )
	slug = models.SlugField(unique=True)

class RSSSource(models.Model):
	name = models.CharField( max_length=100 )
	description = models.CharField( max_length=100 )
	image=models.FileField(upload_to='data/src_img/')
	language = models.CharField( max_length=3 )
	link = models.TextField()

class RSSitem(models.Model):
	RSSSource = models.ForeignKey(RSSSource, on_delete=models.CASCADE)
	title = models.CharField( max_length=100 )
	description = models.CharField( max_length=100 )
	author = models.CharField( max_length=100 )
	link = models.TextField()


