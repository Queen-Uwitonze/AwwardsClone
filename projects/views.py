from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
# # from .email import send_welcome_email
from .models import Profile ,Project
from .forms import NewProfileForm

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()
    profile = Profile.objects.all()
    message = "welcome"
    return render(request, 'home.html',{"message":message,"projects":projects,"profile":profile})

# "projects":projects,"profile":profile
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect("home")

    else:
        form = NewProfileForm()
    return render(request, 'all_gallery/new-profile.html', {"form": form})


def profile(request):
    user = User.objects.get()
    profile = Profile.objects.filter(user = user)
   
    return render(request,'all_gallery/profile.html',{"profile":profile,"user":user})