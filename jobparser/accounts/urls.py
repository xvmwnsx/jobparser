from django.urls import path
from .views import upload_resume, main_page

urlpatterns = [
    path('', main_page, name='main'),
    path('resume/upload/', upload_resume, name='upload_resume'),
]
