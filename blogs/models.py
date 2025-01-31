from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from root.models import Reporter


class Tags(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
            
class Category(models.Model):
    name = models.CharField(max_length= 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Blogs(models.Model):
    name = models.CharField(max_length= 100)
    reporters = models.ForeignKey(Reporter,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tags)
    image = models.ImageField(upload_to='new',default='news.jpg')
    schedule = models.DateTimeField(default= timezone.now)
    content = models.TextField(default='good news')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
      
class Comment(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name.username
    
