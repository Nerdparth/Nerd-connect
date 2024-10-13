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
        return redirect(reverse('home', args=[request.user.username]))
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
        fname = request.POST.get('f.name')
        lname = request.POST.get('l.name')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        bio = request.POST.get('bio')
        course = request.POST.get('course')
        relationship = request.POST.get('relationship')
        tagline = request.POST.get('tagline')
        images = request.FILES.get('image', None)
        user = request.user
        if Details.objects.filter(user = user).exists():
            messages.error(request, "you have already submitted your details")
        else:
            Details.objects.create(user = user, fname = fname, lname = lname, department = department, semester=semester,bio = bio, course = course, relationship=relationship, tagline= tagline, images = images)
            messages.success(request, "account created successfully")
            return redirect(reverse('home', args=[request.user.username]))
    return render(request, "authentication/details.html")

@login_required
def UpdateDetails(request):
    user = request.user

    if request.method == 'POST':
        # Get data from form fields
        fname = request.POST.get('f.name')
        lname = request.POST.get('l.name')
        department = request.POST.get('department')
        semester = request.POST.get('semester')
        bio = request.POST.get('bio')
        course = request.POST.get('course')
        relationship = request.POST.get('relationship')
        tagline = request.POST.get('tagline')
        website = request.POST.get('website')
        instagram = request.POST.get('instagram')
        github = request.POST.get('github')
        facebook = request.POST.get('facebook')
        twitter = request.POST.get('twitter')

        # Get the uploaded image, if any
        images = request.FILES.get('image', None)

        # Update user details
        details = Details.objects.get(user=user)
        details.fname = fname
        details.lname = lname
        details.department = department
        details.semester = semester
        details.bio = bio
        details.course = course
        details.relationship = relationship
        details.tagline = tagline
        details.website = website
        details.instagram = instagram
        details.github = github
        details.facebook = facebook
        details.twitter = twitter
        
        # Only update the image if a new one is provided
        if images:
            details.images = images

        details.save()  # Save changes

        messages.success(request, "Details updated successfully")
        return redirect(reverse('home', args=[request.user.username]))

    return render(request, "home/edit_details.html")

def logout_view(request):
    logout(request)
    messages.success(request, "you have been logged out")
    return redirect(signup)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('home', args=[request.user.username]))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login here
            messages.success(request, 'You have been logged')
            return redirect(reverse('home', args=[request.user.username]))  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')

@login_required
def DeleteAccount(request):
    user = request.user
    deleted_user = User.objects.get(username=user.username)
    logout(request)
    deleted_user.delete()
    messages.success(request, "account deleted successfully")
    return redirect('signup')

def index(request):
    return redirect(signup)