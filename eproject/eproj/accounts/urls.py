from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login_signup', views.login_signup_page, name='login_signup'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout'),

]
