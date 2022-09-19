from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.Job_Listings, name='Job_Listing'),
    path('match-listing/', views.Match_Listings, name='Match_Listing'),
    path('about/', views.About, name = 'about'),
    path('sign_in/', views.Sign_in, name='sign_in'),
    path('sign_up/', views.Sign_up, name='sign_up'),
    path('search/', views.Search, name='search'),
    path('matches/', views.Matches, name='matches'),
    path('saves/', views.Saves, name='saves'),
    path('profile/', views.Profile, name='profile'),
]

