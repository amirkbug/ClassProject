
from django.contrib.auth.models import User

def general_objects(requests):
    context = {
        'users' : User.objects.all().count(),
    }
    return context