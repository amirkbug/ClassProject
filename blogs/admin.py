from django.contrib import admin
from .models import Blogs,Comment,Category,Tags,Reply

admin.site.register(Blogs)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Reply)
