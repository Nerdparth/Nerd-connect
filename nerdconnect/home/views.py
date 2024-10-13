from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posts
from django.contrib import messages
from authentication.models import Details
from django.contrib.auth.models import User



@login_required
def home(request, username):
    user = request.user
    user2 = get_object_or_404(User, username=user.username)
    details = Details.objects.get(user=user)
    fname = details.fname
    lname = details.lname
    relationship = details.relationship
    return render(request, "home/user.html", {"details": details, "fullname" : fname + " " + lname, "relationship" : relationship, "user": user2})

@login_required
def CreatePost(request):
    if request.method == 'POST':
        post = request.POST['post']
        user = request.user
        Posts.objects.create(post = post,user = user)
        messages.success(request, "posted successfully")
    return render(request, "home/create.html")

@login_required
def feedSection(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, "home/feed.html", {"posts" : posts})