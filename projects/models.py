from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True )
    name = models.CharField(max_length=30)
    prof_image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)
    contact = models.CharField(max_length =200,default=0)

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

    # @classmethod
    # def search_by_username(cls,search_term):
    #     profile = cls.objects.filter(first_name__icontains=search_term)
    #     return profile

class Project(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'news/')
    detailed_description = models.CharField(max_length =60)
    link = models.CharField(max_length =200)

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

    @classmethod
    def search_by_project(cls,search_term):
        projects=cls.objects.filter(name__icontains=search_term)
    
        return projects

class ProjectLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Votes(models.Model):
    Design =models.IntegerField(default=0)
    Usability=models.IntegerField(default=0)
    Content=models.IntegerField(default=0)


    @classmethod
    def count_posts(cls,id):
        Votes.objects.all().count()