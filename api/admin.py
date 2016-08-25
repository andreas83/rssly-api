from django.contrib import admin

from models import RSSItem, RSSSource, Category, Reader

admin.site.register(Reader)
admin.site.register(RSSItem)
admin.site.register(RSSSource)
admin.site.register(Category)