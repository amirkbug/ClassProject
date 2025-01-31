from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

class Personaltoken(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=300)
    
    def __str__(self):
        return self.user.email
