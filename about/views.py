from django.shortcuts import render
from .models import Agent, Level

# Create your views here.

def about(request):
    agents = Agent.objects.filter(status=True)
    contex = {
        'agents':agents,
    }
    return render(request, 'about/about.html', context=contex)
