from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from flask import Flask, render_template_string, request
from wtforms import Form, SelectMultipleField
from multiselectfield import multiSelectField


# Create your models here.

SKILLS = (
    ("Javascript", "Javascript"),
    ("HTML", "HTML"),
    ("CSS", "CSS"),
    ("PYTHON", "PYTHON"),
)

class MyUser(AbstractUser):
    skill = SelectMultipleField(
        max_length=15,
        choices= SKILLS
    )

    # skill = models.charField(
    #     max_length=10,
    #     choices = SKILLS,
    #     default = SKILLS[0][0],
    # )
    # matched_jobs
    # saved_jobs



