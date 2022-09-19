from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import requests

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

def Home(request):
     response = requests.get("https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=5e5f3287&app_key=1755dc772df12b9e7aa9c2a0885b6983")
     json = response.json()
     print('this is type of json', type(json))
     results = json['results']
     print('this is results variable', type(results))
     return HttpResponse(results[3]['location']['display_name'])
     
def About(request):
    return HttpResponse('about')
def Sign_in(request):
    return HttpResponse('sign_in')
def Sign_up(request):
    return HttpResponse('sign_up')
def Search(request):
    return HttpResponse('search')
def Sign_up(request):
    return HttpResponse('sign_up')
def Matches(request):
    return HttpResponse('matches')
def Profile(request):
    return HttpResponse('profile')


#json that returns everything related to software engineering jobs 
response = requests.get('https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=5e5f3287&app_key=1755dc772df12b9e7aa9c2a0885b6983&results_per_page=200&what=software')


skills = ['python', 'java', 'html']


def Job_Listings(request):
     #json is a json dictionary that has parsed the request object
     json = response.json()
     #results is an array that (in this case) contains additional dictionaries 
     results = json['results']
     return HttpResponse(results)


def Match_Listings(request):
    matches = []
     #json is a json dictionary that has parsed the request object
    json = response.json()
     #results is an array that (in this case) contains additional dictionaries 
    results = json['results']

    for i in results:
        for s in skills:
            if (i['description'].lower().__contains__(s)):
                matches.append(i['description'])
                break

    return HttpResponse(matches)
 
                




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
     

