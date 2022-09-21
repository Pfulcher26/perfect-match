from django.forms import ModelForm
from .models import Skill
from django.contrib.auth.forms import UserCreationForm
from main_app.models import MyUser

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields  