from . import views
from django.urls import path
urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('submit/<int:assignment_id>/',
         views.submit_assignment, name='submit_assignment'),
    path('detail/<int:pk>/', views.assignment_detail, name='assignment_detail'),]
