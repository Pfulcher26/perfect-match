from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# class Skill(forms.Form):
#     SKILLS = (
#         ("JS", "Javascript"),
#         ("PY", "Python"),
#         ("HTML", "HyperTextMarkupLanguage"),
#     )
#     skill_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
#                                           choices=SKILLS)

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    # def get_absolute_url(self):
    #     return reverse('toys_detail', kwargs={'pk': self.id})
    
class MyUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)



