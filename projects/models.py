from django.db import models
from django.contrib.auth.models import User
import datetime
from vote.models import VoteModel
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True )
    name = models.CharField(max_length=30)
    prof_image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(first_name__icontains=search_term)
        return profile

class Project(VoteModel, models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'news/')
    detailed_description = models.CharField(max_length =60)
    link = models.CharField(max_length =200)
    # score = models.IntegerField(default=0)
    # vote = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects    

    def delete_project(self):
        self.delete()

class ProjectLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()