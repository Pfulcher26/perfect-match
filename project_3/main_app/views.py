from http.client import HTTPResponse
from re import X
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect

from main_app.forms import SkillForm
from .models import MyUser, Skill
import requests

#json that returns everything related to software engineering jobs 
response = requests.get('https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=ce87f4ab&app_key=ccee3366b025e6a97efaa9026117aa9f&results_per_page=200&what=software')

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
    #results is an array that (in this case) contains additional dictionaries 
    results = json['results']

    matches = []

    skill_ids = MyUser.objects.all().values_list('skills')
    current_user_skills = Skill.objects.filter(id__in = skill_ids)

    skills_list = []

    for i in current_user_skills:
        skills_list.append(i)


    print("this is skills_list", skills_list)

    skills = ['python', 'java', 'html'] 
    
    for i in results:
        for s in skills:
            if (i['description'].lower().__contains__(s)):
                matches.append(i['description'])
                break

    return render(request, 'user/job_matches.html', {'matches': matches})

def saved_jobs(request):
    return render(request, 'user/saved_jobs.html')

def profile(request):

    myuser = MyUser.objects.get(id=request.user.id)

    skill_form = SkillForm()

    user = request.user
    current_user = MyUser.objects.filter(id=user.id)
    t = current_user.values_list('skills')
    skills = Skill.objects.filter(id__in = t)
    user_skills = []
    for i in skills:
        user_skills.append(str(i))
        
    return render(request, 'user/profile.html', {'user': user, 'user_skills': user_skills, 'skill_form': skill_form, 'myuser': myuser})
    
def add_skill(request, user_id):

    form = SkillForm(request.POST)
    if form.is_valid():
        new_skill = form.save(commit=False)
        new_skill.user_id = user_id
        print(new_skill)
        new_skill.save()

        x = MyUser.objects.get(id=user_id).skills.add(new_skill.id)
        print('this is x', x)
       

    # MyUser.objects.get(id=skill_id).toys.add(toy_id)
        return redirect('profile')

    #, user_id=user_id


    # current_user_id = request.user.id

    # #display the user skills
    # print("this is current user id", current_user_id)
    # skill_ids = MyUser.objects.filter(id=current_user_id).values_list('skills')
    # print('this is skill_ids', skill_ids)
    # current_user_skills = Skill.objects.filter(id__in = skill_ids)
    # print('this is curren_user_skills', current_user_skills)
    # # print('this is first index', current_user_skills.Skill[0])

    # skills_list = []

    # # for i in current_user_skills:
    # #     skills_list.append(current_user_skills[i])


    # print("this is skills_list", skills_list)

    # # user = MyUser.objects.filter(email=current_user.email)
    #  return render(request, 'user/profile.html')
    # #    return render(request, 'user/profile.html', {'user': user})

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