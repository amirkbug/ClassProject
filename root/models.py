from django.db import models
from accounts.models import Profile

    

class Skills(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)

class Reporter(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reporter',default= 'unknown.jpg')
    skills = models.ManyToManyField(Skills)
    content = models.TextField(default='good reporter')
    twitter = models.CharField(max_length= 120,blank=True,null=True)
    instagram = models.CharField(max_length= 120,blank=True,null=True)
    facebook = models.CharField(max_length= 120,blank=True,null=True)
    linkedin = models.CharField(max_length= 120,blank=True,null=True)
    status = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.user.username
    
    class Mata:
        ordering = ('created_at',)
        
class Contactus(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.email
