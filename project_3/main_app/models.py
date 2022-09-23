from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    #def __str__(self):
     #   return f"Photo for cat_id: {self.cat_id} @{self.url}"

class Job_listing():
    def __init__(self, description, title, company_display_name, category_label, location_display_name, job_id, redirect_url):
        self.description = description
        self.title = title
        self.company_display_name = company_display_name
        self.category_label = category_label
        self.location_display_name = location_display_name
        self.job_id = job_id
        self.redirect_url = redirect_url
        self.saved = False

class Job(models.Model):
    description = models.TextField()
    title = models.TextField()
    company_display_name = models.TextField()
    category_label = models.TextField()
    location_display_name = models.TextField()
    job_id = models.BigIntegerField()
    job_posting_url = models.TextField()
    
class MyUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)
    saved_jobs = models.ManyToManyField(Job)

class Resume(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    



        
