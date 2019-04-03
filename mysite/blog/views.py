from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from .models import Post
from .forms import PostCreateForm,UserLoginForm,UserRegistrationForm

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'blog/post_list.html',context)


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostCreateForm()
    context = {
        'form':form,

    }
    return render(request, 'blog/post_create.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('blog:post_list'))
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is none')
    else:
        form = UserLoginForm()
    

    context = {
        'form':form,
    }

    return render(request, 'blog/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('blog:post_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commmit=False)
            new_user.self_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('blog:post_list')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form
    }

    return render(request, 'registration/register.html',context)
