from django.shortcuts import render, get_object_or_404, redirect
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
        return redirect(feedSection)
    return render(request, "home/create.html")

@login_required
def feedSection(request):
    posts = Posts.objects.all().order_by('-created_at')

    # Prepare a list of posts with related user details
    posts_with_details = []
    for post in posts:
        # Fetch the details for each post's user
        details = Details.objects.filter(user=post.user).first()  # Use .first() to avoid exceptions
        posts_with_details.append({
            'post': post,
            'details': details
        })

    return render(request, "home/feed.html", {"posts_with_details": posts_with_details})


@login_required
def UserPosts(request):
    user = request.user
    username = user.username
    image_getter = Details.objects.get(user = user)
    images = image_getter.images
    posts = Posts.objects.filter(user = user)
    return render(request, "home/userposts.html", {"post": posts, "user" : username, "images" : images})

def SomeUser(request, username):
    user = get_object_or_404(User, username=username)
    details = Details.objects.get(user=user)
    fullname = f"{details.fname} {details.lname}"
    return render(request, "home/profile.html", {"details": details, "fullname": fullname, "user": user})

def Search(request):
    users = None
    query = None
    if request.method == 'POST':
        query = request.POST['search']
        if query:
            users = User.objects.filter(username__icontains=query)
        else:
            users = User.objects.none()
    return render(request, "home/search.html", {"users" : users, "query": query})


