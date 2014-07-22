__author__ = 'albertlwohletz'
import models
from django.shortcuts import render

# To be replaced by Confluence API in final implementation.
def request_access(request):
    type = request.GET['type']
    space_name = request.GET['space_name']
    reason = request.GET['reason']

    # Get Space
    new_space = models.Spaces.objects.get(name=space_name)

    # Get User
    user = request.user

    req = models.Pending(user=user, space=new_space, access_type=type, explanation_string=reason)
    req.save()
    return render(request, 'base_template.html', {})

def manage_request(request, approve):
    user_name = request.GET['user']
    space_name = request.GET['space_name']

    # Get Space
    space = models.Spaces.objects.get(name=space_name)

    # Get User
    user = models.User.objects.get(username=user_name)

    # Save New Access If Approved
    if approve:
        access = request.GET['access']
        new = models.Access(user=user, space=space, access_type=access)
        new.save()

    # Delete Access Request
    models.Pending.objects.filter(user=user, space=space).delete()

    return render(request, 'base_template.html', {})

def approve_request(request):
    manage_request(request, True)

    return render(request, 'base_template.html', {})

def remove_request(request):
    manage_request(request, False)

    return render(request, 'base_template.html', {})

