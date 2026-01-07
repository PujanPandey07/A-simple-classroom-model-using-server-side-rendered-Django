from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [path('', views.account_home, name='account_home'),
               path('login/', views.login_view, name='login'),
               path('register/', views.register_view, name='register'),
               path('logout/', views.logout_view, name='logout'),
               path('dashboard/', views.dashboard,
                    name='my_dashboard'),]
