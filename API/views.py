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