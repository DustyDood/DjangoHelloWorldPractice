from django.http import HttpResponse
from django.shortcuts import render
#We would want to import Userprofile from
#from ..profiles.models import UserProfile
#But this THROWS an error, as it exceeds our top-level application

def home(request):
    names = "Dusty"

    context = {
        'names': names,
    }

    return render(request, "home.html", context)