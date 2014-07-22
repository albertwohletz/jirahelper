__author__ = 'albertlwohletz'
import models
from django.contrib.auth.models import User

# To be replaced by Confluence API in final implementation.
def request_access(request):
    type = request.GET['type']
    space_name = request.GET['space_name']
    reason = request.GET['reason']

    # Get Space
    new_space = models.Spaces.objects.filter(name__=space_name)
    # Get User

    req = models.Pending(user=User, space=new_space, access_type=type, explanation_string=reason)
