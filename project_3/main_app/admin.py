from django.contrib import admin
from .models import MyUser, Skill

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Skill)