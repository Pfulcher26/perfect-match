from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django import forms


# Create your models here.

SKILLS = (
    ("Javascript", "Javascript"),
    ("HTML", "HTML"),
    ("CSS", "CSS"),
    ("PYTHON", "PYTHON"),
)

class MyUser(AbstractUser):
    # skill = SelectMultipleField(
    #     max_length=15,
    #     choices= SKILLS
    # )
    # BOOK_CHOICES = (
    #     ('Book1', "Book1"),
    #     ("Book2", "Book2"),
    #     ("Book3", "Book3"),
    #     ("Book4", "Book4"),
    # )

    name = "Hello"

    # title = MultiSelectField(choices = BOOK_CHOICES)

    # skill = models.charField(
    #     max_length=10,
    #     choices = SKILLS,
    #     default = SKILLS[0][0],
    # )
    # matched_jobs
    # saved_jobs



