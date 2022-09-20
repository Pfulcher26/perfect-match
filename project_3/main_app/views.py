from http.client import HTTPResponse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
import requests

# from django.contrib.auth.backends import BaseBackend

# from .models import User, Skill, Job, Company



Headers = {
  "access-control-allow-headers": "Origin, X-Requested-With, Content-Type, Accept",
  "access-control-allow-origin": "*",
  "connection": "keep-alive",
  "content-encoding": "gzip",
  "content-length": "4281",
  "content-type": "application/json; charset=utf8",
  "date": "Mon, 19 Sep 2022 21:24:59 GMT",
  "server": "openresty",
  "vary": "Content-Type",
  "x-catalyst": "5.90129",
  "x-envoy-upstream-service-time": "711",
}

def Home(request):
     response = requests.get("https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=5e5f3287&app_key=1755dc772df12b9e7aa9c2a0885b6983")
     json = response.json()
     print('this is type of json', type(json))
     results = json['results']
     print('this is results variable', type(results))
     return HttpResponse(results[3]['location']['display_name'])
     
def About(request):
    return render(request, 'about')

def Sign_in(request):
    return render(request, 'sign_in')

def Sign_up(request):
    return render(request, 'sign_up')

def Search(request):
    return render(request, 'search')

def Matches(request):
    return render(request, 'matches')

def Profile(request):
    return render(request, 'profile')

def Saves(request):
    return render(request, 'saves')

def Company(request):
    return render(request, 'company')
#user autho

# 
# class JobDetail(LoginRequiredMixin, DetailView):
#     model = Job

# class JobDelete(LoginRequiredMixin, DeleteView):
#     model = Job

# class DeleteMatch(LoginRequiredMixin, DeleteView):
#     model = Job

# class CreateSkill(LoginRequiredMixin, CreateView): # add skill form
#     model = Skill

# class DeleteSkill(LoginRequiredMixin, DeleteView): 
#     model = Skill

# class CompanyDetail(LoginRequiredMixin, DetailView):
#     model = ACompany





    
# Create your views here.
