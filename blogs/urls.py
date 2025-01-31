from django.urls import path 
from .views import *

app_name = 'blogs'

urlpatterns = [
    path('',blogs , name = 'blogs'),
    path('category/<str:catname>',blogs , name = 'blogs_category'),
    path('details/<int:id>',blogs_detail , name = 'blogs_detail')
]