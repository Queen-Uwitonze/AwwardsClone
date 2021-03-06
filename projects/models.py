from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
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
    
    def update_bio(self,bio):
        self.bio = bio
        self.save()
        
    @classmethod
    def search_by_name(cls,search_term):
        profile = cls.objects.filter(name__icontains=search_term)
        return profile
    
class Project(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length =60)
    post = models.ImageField(upload_to = 'images/')
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
    def search_project(cls,search_term):
        projects=cls.objects.filter(name__icontains=search_term)
    
        return projects

class ProjectLetterForm(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Votes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    posted_on = models.DateTimeField(default=datetime.datetime(2015, 12, 26, 17, 1, 28, 128127))
    project =  models.ForeignKey(Project,on_delete=models.CASCADE,default=True)
    design = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    usability = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    content = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))


    def __str__(self):
        return self.user
    
    def save_votes(self):
        self.save()