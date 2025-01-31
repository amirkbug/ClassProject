from django.shortcuts import render,redirect,get_object_or_404
from .form import *
from django.contrib.auth import authenticate,login,logout,password_validation
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Personaltoken
from uuid import uuid4
from django.core.mail import send_mail

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/login.html',context=context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username_or_email']
            if '@' in username:
                user = get_object_or_404(User,email = username)
                name = user.username
                password = form.cleaned_data['password']
                user = authenticate(username =name,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'please enter your data in correct way')
                    return redirect(request.path_info)
            else:
                username = form.cleaned_data['username_or_email']
                password = form.cleaned_data['password']
                user = authenticate(username = username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'please enter your data in correct way')
                    return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "Login failed please check you input data and try again ")
            return redirect(request.path_info)
@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request): 
    if request.method == 'GET':
        form = SignupForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/signup.html',context=context)
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'havnet save please try again ')
            return redirect(request.path_info)
@login_required       
def change_password(request):
    if request.method == 'GET':
        form = Change_passwordForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/change_password.html',context=context)
    elif request.method == 'POST':
        user = request.user
        current_password = request.POST.get('current_password')
        if not user.check_password(current_password):
            messages.add_message(request,messages.ERROR,'your current password isnt match')
            return redirect(request.path_info)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            messages.add_message(request,messages.ERROR,'the new passwords have to be the same as each other')
            return redirect(request.path_info)
        try:
            password_validation.validate_password(password)
            user.set_password(password)
            user.save()
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'your password have been changed')
            return redirect('/')
        except:
            messages.add_message(request,messages.ERROR,'password validation is failed')
            return redirect(request.path_info)
        
        
        
        
def reset_password(request):
    if request.method == 'GET':
        form = ResetpasswordForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/reset_password.html',context=context)
    else:
        form = ResetpasswordForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User,email=form.cleaned_data['email'])
            try:
                token = Personaltoken.objects.get(user=user)
            except:
                token = Personaltoken.objects.create(user=user,token=str(uuid4()))
            send_mail(
                'reset password',
                f'http://127.0.0.1:8000/accounts/reset_password_confirm/{token.token}',
                'admin',
                [user.email],
                fail_silently=True
            )
            return redirect('accounts:reset_password_done')
        else:
            messages.add_message(request,messages.ERROR,'please enter the correct email')
            return redirect(request.path_info)
            
            
def reset_password_done(request):
    return render(request,'accounts/reset_password_done.html')

def reset_password_confirm(request,token):
    if request.method == 'GET':
        form = ResetpaswordconfirmForm()
        context = {
            'form':form,
        }
        return render(request,'accounts/reset_password_confirm.html',context=context)
    else:
        user = Personaltoken.objects.get(token=token).user
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.add_message(request,messages.ERROR,'they have to be thes same as eachother')
            return redirect(request.path_info)
        try:
            password_validation.validate_password(pass1)
            user.set_password(pass1)
            user.save()
            return redirect('accounts:reset_password_complete')
        except:
            messages.add_message(request,messages.ERROR,'password validation is failed')
            return redirect(request.path_info)
        

def reset_password_complete(request):
    return render(request,'accounts/reset_password_complete.html')
    
        