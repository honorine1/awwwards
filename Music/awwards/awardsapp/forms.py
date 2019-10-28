from django import forms
from .models import Profile,Projects


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['profile','user', 'created_date']
        

