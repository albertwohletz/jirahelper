from django.shortcuts import render
from API import models

# Create your views here.
def default(request):
    return render(request, 'base_template.html', {})

def request_access(request, space_name):
    return render(request, 'base_template.html', {})

def request_page(request):
    spaces = models.Spaces.objects.all()
    context = {'spaces': spaces}
    return render(request, 'spaces.html', context)