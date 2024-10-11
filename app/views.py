from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from app.models import JobPost

job_titles = [
    "First Job",
    "Second Job",
    "Third Job",
]

job_descriptions = [
    "First job descripton",
    "Second job descripton",
    "Third job description",
]



def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, 'app/index.html', context)



def job_detail(request, id):
    if id == 0:
        return redirect(reverse('jobs_home'))
    job = JobPost.objects.get(id = id)
    context = {"job":job}
    return render(request, 'app/job_detail.html', context)