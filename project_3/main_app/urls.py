from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/<int:user_id>/initial_skills', views.initial_skills, name='initial_skills'),
    path('accounts/signup/<int:user_id>/add_initial_skills', views.add_initial_skills, name='add_initial_skills'),
    path('accounts/<int:user_id>/<int:skill_id>/delete-skill', views.delete_skill, name='delete_skill'),
    path('job-listings/', views.job_listings, name = 'job_listings'),
    path('job-matches/', views.job_matches, name='job_matches'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/add-skill/', views.add_skill, name='add_skill'),
    path('about/', views.about, name = 'about'),
    path('searchbar/', views.searchbar, name ='searchbar'),

]

