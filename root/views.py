from django.shortcuts import render,redirect
from .models import Reporter
from .form import Contactusform
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'root/index.html') 

def contact(request):
    if request.method == 'GET':
        return render(request,'root/contact.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            form = Contactusform(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'we recieve your message and will answer you soon')
                return redirect(request.path_info)
            else:
                messages.add_message(request,messages.ERROR,'please try again')
                return redirect('root:contact')
        else:
            return redirect('accounts:login')

def about(request):
    reporters = Reporter.objects.filter(status = True)
    context = {
        'reporters' : reporters
    }
    return render(request,'root/about.html',context=context)
