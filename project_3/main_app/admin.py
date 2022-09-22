from django.contrib import admin
from .models import Job, MyUser, Skill

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Skill)
admin.site.register(Job)

