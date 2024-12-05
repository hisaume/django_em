from django.shortcuts import render
from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects':projects})

def project_detail(request):
    project = Project.objects.all()
    return render(request, 'projects/project_detail.html', {'project': project})
