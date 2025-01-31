from django.shortcuts import render, get_object_or_404,redirect
from .models import Comment,Reply,Blogs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm,ReplyForm
from django.contrib import messages


def blogs(request,**kwargs):
    if request.GET.get('search') is not None:
        blog = Blogs.objects.filter(content__contains = request.GET.get('search'))
    elif kwargs.get('catname'):
        blog = Blogs.objects.filter(category__name = kwargs.get('catname'))
    else:
        blog = Blogs.objects.filter(status = True)
        
    context = {
        'blog' : blog,
    }
    return render(request,'blogs/blogs.html',context=context)

def blogs_detail(request,id):
    if request.method == 'GET':
        blog = get_object_or_404(Blogs,id=id)
        comments = Comment.objects.filter(status = True,blogs = blog)
        reply = Reply.objects.filter(status = True)
        context = {
            'blog':blog,
            'comments' : comments,
            'reply':reply,    
        }
        return render(request,'blogs/single-post.html',context=context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'your comment have been sent')
                return redirect(request.path_info)
            else:
                messages.add_message(request,messages.ERROR,'please try again')
                return redirect(request.path_info)
        else:
            return redirect('accounts:login')