from django.forms import ModelForm
from .models import Skill
from django.contrib.auth.forms import UserCreationForm
from main_app.models import MyUser
from django.utils.translation import gettext_lazy as _
from django import forms


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email',)
