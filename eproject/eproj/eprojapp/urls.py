from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_page, name='home'),
    path('jobs', views.job_page, name='jobs'),
    path('forms', views.form_name_view, name='forms'),
    path('list', views.tokens_list, name='list'),
    path('about', views.about_page, name='about'),
]
