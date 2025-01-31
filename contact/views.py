from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm

def contact(request):
    form = ContactMessageForm()
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
            return redirect(request.path)  # ریدایرکت به همان صفحه برای حل مشکل ارسال مجدد

    return render(request, 'contact/contact_form.html', {'form': form})
