from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.Job_Listings, name='Job_Listing'),
    path('match-listing/', views.Match_Listings, name='Match_Listing')
]