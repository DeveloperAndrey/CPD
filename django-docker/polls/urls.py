from django.urls import path
from . import views

urlpatterns = [
    #path('kakashkacherezk', views.index, name ='index'),

    path('claster', views.claster_all, name='claster'),

    path('claster/<int:filter>', views.claster_filter, name='clasterFilter'),

    path('project', views.project_all, name='project_all'),

    path('project/<int:filter>', views.project_filter, name='project_filter'),
]
