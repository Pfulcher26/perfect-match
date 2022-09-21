from django.forms import ModelForm
from .models import Skill


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name']