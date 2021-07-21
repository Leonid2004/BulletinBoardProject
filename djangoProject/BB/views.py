from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView
from django.views.generic import DetailView
from .models import Post,Messages
from django.contrib.auth.models import User
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
    fields = ['title', 'text','Category','filesForWeb']
    template_name = "addPost.html"

    def form_valid(self, form):
        return redirect("/posts/")








