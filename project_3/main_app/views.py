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

# Create your views here.
