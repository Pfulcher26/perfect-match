from http.client import HTTPResponse
from re import X
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import MyUser, Skill, Job
from main_app.forms import SkillForm, CustomUserCreationForm
from .models import MyUser, Skill
import requests
# login imports 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



#json that returns everything related to software engineering jobs 
response = requests.get('https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=d77f8a15&app_key=cfbfca3c016e2c88fb67412299052d58&results_per_page=200&what=software')
job_list = []
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('initial_skills', user_id = request.user.id)
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = CustomUserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def initial_skills(request, user_id):
    skill_form = SkillForm()
    return render(request, 'registration/initial_skills.html', {'skill_form': skill_form, 'user_id': user_id})

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
            new_object = Job(i['description'], i['title'], i['company'], i['category'], i['location'], i['id'], i['redirect_url'])
            
            job_list.append(new_object)
            
        # renders the html with the results list 
        return render(request, 'job/job_listings.html', {'results_list': results_list})

@login_required
def job_matches(request): 
    #json is a json dictionary that has parsed the request object
    json = response.json()
    #results is an array that (in this case) contains additional dictionaries 
    results = json['results']
    matches = []
    current_user = request.user
    user = MyUser.objects.filter(id=current_user.id)
    t = user.values_list('skills')
    skills = Skill.objects.filter(id__in = t)
    # list of all user skills
    skill_list = []
    for i in skills:
        skill_list.append(str(i))
    # list of all skill matches
    matches = []
    # iterates
    for i in results:
        for j in skill_list:
            if (i['description'].lower().__contains__(j.lower())):
                matches.append(i)
                break 
    return render(request, 'user/job_matches.html', {'matches': matches})

@login_required
def saved_jobs(request):
    return render(request, 'user/saved_jobs.html')

@login_required
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

        return redirect('profile')
       
def searchbar(request):
        matched_arr = []
        if request.method == 'GET':
            search = request.GET.get('search')

            for i in job_list:
                if i.description.lower().__contains__(search):
                    matched_arr.append(i)

        return render(request, "job/searchbar.html", {'matched_arr': matched_arr})


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