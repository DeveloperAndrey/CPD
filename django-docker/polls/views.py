from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from .models import Claster, Project

from django.views.decorators.csrf import csrf_exempt

def index(request):
    User = get_user_model()
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
    return HttpResponse("Hello world, вы в polls")

def claster_all(request):
    clast = Claster.objects.all()
    clast_json = serializers.serialize('json', clast)
    return HttpResponse(clast_json, content_type='application/json')

def claster_filter(request,filter):
    clast = Project.objects.filter(cluster__pk = filter)
    clast_json = serializers.serialize('json', clast)
    return HttpResponse(clast_json, content_type='application/json')

@csrf_exempt
def project_all(request):
    project = Project.objects.all()
    project_json = serializers.serialize('json', project)
    return HttpResponse(project_json, content_type='application/json')
    
@csrf_exempt
def project_filter(request,filter):
    clast = Project.objects.filter(pk = filter)
    clast_json = serializers.serialize('json', clast)
    return HttpResponse(clast_json, content_type='application/json')