from django.db import models

# Create your models here.

class Level(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Agent(models.Model):
    name = models.CharField(max_length=120)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    img = models.ImageField(upload_to="agent", default="defaault.jpg")

    def __str__(self):
        return self.name

