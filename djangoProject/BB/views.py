from django.shortcuts import render
from django.views.generic import ListView
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
