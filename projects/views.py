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
from .permissions import IsAdminOrReadOnly

@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()
    grades= Votes.objects.filter().all()
    profile = Profile.objects.get()
    message = "welcome"
    return render(request, 'home.html',{"message":message,"projects":projects,"profile":profile,"grades":grades})


class ProfileList(APIView):
    
    def get (self,request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)
        permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(profile_pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

def ProjectLetterForm(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

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
    return render(request, 'all_gallery/new-profile.html',{"form": form})


def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    print(profile.user_id)
    return render(request,'all_gallery/profile.html',{"profile":profile})

def more(request):
    return render(request,'all_gallery/details.html')

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
    return render(request,"all_gallery/details.html", {"projects":projects})

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        projects = Project.search_project(search_term)
        message=f"{search_term}"
        return render(request,'search.html',{"message":message,"projects":projects,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def votes(request,id):
    current_user = request.user
    post = Project.objects.get(id=id)
    votes = Votes.objects.get(project=id)
  
    if request.method == 'POST':
            vote = VotesForm(request.POST)
            if vote.is_valid():
                design = vote.cleaned_data['design']
                usability = vote.cleaned_data['usability']
                content = vote.cleaned_data['content']
                rating = Votes(design=design,usability=usability,content=content,user=request.user,project=post)
                rating.save()
                return redirect('project')      
    else:
        form = VotesForm()
        return render(request, 'vote.html', {"form":form,'post':post,'user':current_user,'votes':votes})