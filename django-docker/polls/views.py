from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.template import loader
from .models import Claster, Project

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index_(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mail = request.POST.get("mail")
        password = request.POST.get("password")
        User = get_user_model()
        User.objects.create_superuser(name, mail, password)
        return HttpResponse("Hello world, вы в polls")

def index(request):
    return render(request, 'index.html')
def about_us(request):
    return render(request, 'Abous_us.html')
def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def claster_all(request):
    clast = Claster.objects.all()


@csrf_exempt
def claster_filter(request, filter):
    clast = Project.objects.filter(cluster__pk = filter)
    return render(request, 'Project.html', {"data": clast})

@csrf_exempt
def project_all(request):
    project = Project.objects.all()
    return render(request, 'Project.html', {"data": project})


@csrf_exempt
def project_filter(request,filter):
    project = Project.objects.filter(pk = filter)
    return render(request, 'Project_deteil.html', {"data": project})