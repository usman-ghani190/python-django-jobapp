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

# Create your views here.
# def hello(request):
#     return HttpResponse("<h1>Hello World</h1>")

def hello(request):
    # template = loader.get_template('app/hello.html')
    l = ["aslam", "khan", "sir"]
    is_authenticated = True
    context = {"name": "Django", "first_list": l, "age": 14, "is_authenticated": is_authenticated}
    # return HttpResponse(template.render(context, request))
    # render(request-object, template, context)
    return render(request, "app/hello.html", context)



def job_list(request):
    # list_of_jobs = "<ul>"
    # for i in job_titles:
    #     job_id = job_titles.index(i)
    #     print(reverse('job_detail',args=(job_id,)))
    #     list_of_jobs += f"<li><a href = 'job/{job_id}'>{i} </a></li>"
    #     context= {"list_os_jobs": list_of_jobs, "job_id": job_id, "job_titles": job_titles}
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    if id == 0:
        return redirect(reverse('jobs_home'))
    job = JobPost.objects.get(id = id)
    context = {"job":job}
    # return_html = f"<h1>{job_titles[id]}</h1> <h3>{job_descriptions[id]}</h3>"
    # return HttpResponse(return_html)
    return render(request, "app/job_detail.html", context)