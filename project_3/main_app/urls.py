from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('job-listings/', views.job_listings, name = 'job_listings'),
    path('job-matches/', views.job_matches, name='job_matches'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name = 'about'),
    # path('jobs/<int:user_id>/assoc_skill/<int:skill_id>/',
    #      views.assoc_skill, name="assoc_skill"),
    path('jobs/<int:myuser_id>/add_skill/',
         views.add_skill, name="add_skill")
]

