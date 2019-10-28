from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
# Create your models here.



class Profile(models.Model):
    profile_pic =  models.ImageField(default='default.jpg',upload_to = 'profile_pics/', blank=True, null=True) 
    bio = models.TextField(max_length = 200,null=True)
    contact  = models.IntegerField(default=None,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
        
    @classmethod
    def delete_profile(cls,profile):
        cls.objects.filter(profile=profile).delete()

class Projects(models.Model):
    proTitle = models.CharField(max_length=50)
    proImage =  models.ImageField(upload_to = 'project_pics/', blank=True)
    proDesc = HTMLField()
    proLink = models.URLField(max_length=200)
    profile = models.ForeignKey(Profile,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proTitle 
    def save_projects(self):
        self.save()

    @classmethod
    def delete_projects(cls,project):
        cls.objects.filter(project=project).delete()

    @classmethod
    def search_by_proTitle(cls,search_term):
        projects = cls.objects.filter(proTitle__icontains=search_term)
        return projects

