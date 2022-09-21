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

    skills = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: skills',
                         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Skills'}))

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('skills',)
