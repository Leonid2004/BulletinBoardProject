from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView
from django.views.generic import DetailView
from .models import Post,Messages
from django.contrib.auth.models import User
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class Main(ListView):
    model = Post
    template_name = "main.html"
    context_object_name = "theUnusedVariable"


class PostsList(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "thePost"

class theAccountList(ListView):
    model = Post
    template_name = "theAccount.html"
    context_object_name = "theAcc"

class RegistrationPage(ListView):
    model = User
    template_name = "toRegistrate.html"
    context_object_name = "trg"

    def post(self,request,*args,**kwargs):
        userMail_ = request.POST['theMail']
        thePassword_ = request.POST['thepassword']
        userUsername_ = request.POST['theUsername']

        usrAdd = User(username=userUsername_, email=userMail_)
        usrAdd.set_password(thePassword_)
        usrAdd.save()
        return super().get(request,*args,**kwargs)

# class addPostPage(ListView):
#     model = Post
#     template_name = "addPost.html"
#     context_object_name = "tttPost"

class addPostPage(CreateView):
    model = Post
    form_class = PostForm
    template_name = "addPost.html"
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        Post = form.save()
        Post.save()
        form.save()
        return redirect("/posts/")


class singlePost(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "APost"






