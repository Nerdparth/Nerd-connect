from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=30, choices=[('Single', 'Single'), ('In relationship', 'In relationship')], default="Single")
    tagline = models.CharField(max_length= 300, default="GNDU student")
    fname = models.CharField(max_length=60, default="i don't remember")
    lname = models.CharField(max_length=60,default="i don't remember")
    department = models.CharField(max_length=60,default="-")
    course = models.CharField(max_length=60, default="NON-USEFUL")
    semester = models.CharField(max_length=60, choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('graduated', 'graduated') ], default='1')
    bio = models.CharField(max_length=60, default='Oops i just forgot to add my Bio')
    website = models.URLField(default="-")
    instagram = models.URLField(default="-")
    github = models.URLField(default="-")
    facebook = models.URLField(default="-")
    twitter = models.URLField(default="-")
