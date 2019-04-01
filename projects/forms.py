from django import forms
from django.core.files import File
from .models import Profile,Project,Votes

class ProjectLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class VotesForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user']