from django.urls import path
from .views import submission_reviews

urlpatterns = [
    path('submission/<int:submission_id>/',
         submission_reviews,
         name='submission_reviews'),
]
