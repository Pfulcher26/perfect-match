from http.client import HTTPResponse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyUser, Skill
import requests

#json that returns everything related to software engineering jobs 
response = requests.get('https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=177ec933&app_key=e386235bc03cab32af619d4170578653&results_per_page=200&what=software')

# from django.contrib.auth.backends import BaseBackend

# from .models import User, Skill, Job, Company

# Create your views here.

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

def home(request):
    return render(request, 'home.html')

def log_in(request):
    return render(request, 'registration/log_in.html')

def sign_up(request):
    return render(request, 'registration/sign_up.html')

def job_listings(request):
        # Look into refactoring 
        #json is a json dictionary that has parsed the request object
        json = response.json()
        #results is an array that (in this case) contains additional dictionaries 
        results = json['results'] 
        # Creates a results list 
        results_list = []
        # appends all job descriptions to the list 
        for i in results:
            results_list.append(i)
        # renders the html with the results list 
        return render(request, 'job/job_listings.html', {'results_list': results_list})


def job_matches(request):
    
    #json is a json dictionary that has parsed the request object
    json = response.json()
    # results is an array that (in this case) contains additional dictionaries 
    results = json['results']
    # current_user = request.user
    skills_arr = []
    matches = []
    # t = MyUser.objects.all().values_list('skills')
    # current_user = MyUser.objects.get(id__in = t)
    # skills = current_user.skills
    # print(t)


    user = MyUser.objects.get(name="test2")
    skills_user_has = Skill.objects.filter(id__in = user.skills.all().values_list('id'))
    # print(skills_user_has)

    for s in skills_user_has:
        skills_arr.append(str(s))

    for i in results:
        for j in skills_arr:
            if (i['description'].lower().__contains__(j)):
                matches.append(i)
                break

    return render(request, 'user/job_matches.html', {'matches': matches})

def saved_jobs(request):
    return render(request, 'user/saved_jobs.html')

def profile(request):
    current_user = request.user
    user = MyUser.objects.filter(email=current_user.email)
    return render(request, 'user/profile.html', {'user': user})

def about(request):
    return render(request, 'about.html')




# # def Company(request):
#     return render(request, 'company.html')

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


#  for i in results:
    #     if ()
    #     print(i['description'])






# def Home(request):
#      response = requests.get("https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=5e5f3287&app_key=1755dc772df12b9e7aa9c2a0885b6983")
#      json = response.json()
#      print('this is type of json', type(json))
#      results = json['results']
#      print('this is results variable', type(results))
#      return HttpResponse(results[3]['location']['display_name'])