
from django.urls import path

# from app.views import hello, job_detail
from app import views


urlpatterns = [
    path('', views.job_list, name='jobs_home'),
    # path('job/1', views.job_detail), #static url
    # path('hello/', views.hello, name= 'hello'),
    path('job/<int:id>', views.job_detail, name='job_detail'), #dynamic url
]