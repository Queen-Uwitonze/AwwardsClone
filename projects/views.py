from django.shortcuts import render,redirect
from django.http  import Http404
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from .forms import GalleryLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
# # from .email import send_welcome_email
from .models import Profile ,Project,Votes
from .forms import NewProfileForm,ProjectForm,VotesForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile,Project ,Votes
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()
    profile = Profile.objects.all()
    num= Votes.objects.all().count()
    message = "welcome"
    return render(request, 'home.html',{"message":message,"projects":projects,"profile":profile,"num":num})

class ProfileList(APIView):
    def get (self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    def get(self,request):
        project = Project.objects.all()
        serializer=ProjectSerializer(project,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


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
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
   
    return render(request,'all_gallery/profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def projects(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = current_user
            projects.profile = current_user
            projects.save()

        return redirect("home")

    else:
        form = ProjectForm()
    return render(request, 'projects.html', {"form": form})

@login_required(login_url='/accounts/login/')
def photo(request,projects_id):
    projects = Project.objects.get(id = projects_id)
    return render(request,"all_gallery/details.html", {"projects":projects,})

@login_required(login_url='/accounts/login/')
def votes(request):
    num= Votes.objects.all().count()
    current_user = request.user
    if request.method == 'POST':
        form = VotesForm(request.POST, request.FILES)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = current_user
            vote.projects = current_user
            vote.save()

        return redirect("all_gallery/details.html")

    else:
        form = VotesForm()
    return render(request, 'vote.html', {"form": form,"num":num})

