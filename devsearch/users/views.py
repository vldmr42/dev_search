from django.shortcuts import render

# Create your views here.
from users.models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'users/profiles.html', context)