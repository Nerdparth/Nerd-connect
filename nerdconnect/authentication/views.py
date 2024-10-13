from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from home.views import home
from .models import Details
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
        elif password != confirm_password:
            messages.error(request, "passwords do not match")
        else:
            user = User.objects.create_user(username, email, password)
            login(request, user)
            return redirect(detail_section)
            
    return render(request, "authentication/signup.html")

@login_required
def detail_section(request):
    if request.method == 'POST':
        fname = request.POST['f.name']
        lname = request.POST['l.name']
        department = request.POST['department']
        semester = request.POST['semester']
        bio = request.POST['bio']
        course = request.POST['course']
        relationship = request.POST['relationship']
        tagline = request.POST['tagline']
        user = request.user
        if Details.objects.filter(user = user).exists():
            messages.error(request, "you have already submitted your details")
        else:
            Details.objects.create(user = user, fname = fname, lname = lname, department = department, semester=semester,bio = bio, course = course, relationship=relationship, tagline= tagline)
            return redirect(reverse('user_profile', args=[request.user.username]))
    return render(request, "authentication/details.html")

@login_required
def UpdateDetails(request):
    user=request.user

    if request.method == 'POST':
        fname = request.POST['f.name']
        lname = request.POST['l.name']
        department = request.POST['department']
        semester = request.POST['semester']
        bio = request.POST['bio']
        course = request.POST['course']
        relationship = request.POST['relationship']
        tagline = request.POST['tagline']
        user = request.user
        website = request.POST['website']
        instagram = request.POST['instagram']
        github = request.POST['github']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        Details.objects.filter(user=user).update(fname=fname,lname=lname,department=department,semester=semester,bio=bio,course=course,relationship=relationship,tagline = tagline,website=website,instagram=instagram,github=github,facebook=facebook,twitter=twitter)
        return redirect(reverse('user_profile', args=[request.user.username]))
    return render(request, "home/edit_details.html")

def logout_view(request):
    logout(request)
    messages.success(request, "you have been logged out")
    return redirect(signup)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login here
            messages.success(request, 'You have been logged')
            return redirect(reverse('user_profile', args=[request.user.username]))  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')

def DeleteAccount(request):
    user = request.user
    deleted_user = User.objects.get(username=user.username)
    deleted_user.delete()
    logout(request)
    return redirect('signup')