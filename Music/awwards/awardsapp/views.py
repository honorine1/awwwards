from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ProjectsForm
from .models import User,Profile,Projects

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    proImages= Projects.objects.all().order_by("posted_date")
    profile= Profile.objects.all()
    return render(request,'all-awards/index.html',{"proImages":proImages},{"profile":profile})
    # return render(request,'all-awards/index.html')

@login_required(login_url='/accounts/login/')
def project_posts(request, post_id):
    try:
        posts = Projects.objects.all().order_by('posted_date')
       
    except DoesNotExist:
        raise Http404()
    return render(request,"all-awards/project_post.html", {"posts":posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            projects = form.save(commit=False)
            projects.user = current_user
            projects.save()
            return redirect('index')

    else:
        form = ProjectsForm()
    return render(request, 'all-awards/post_form.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    current_user = request.user.username
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')

    else:
        form = ProfileForm()

    user=User.objects.all()

    proImage = Projects.objects.filter(user__username=current_user)


    profile = Profile.objects.filter(user__username = current_user)

    return render(request,"all-awards/profile.html",{"user":user,"proImages":proImage,"profile":profile})



@login_required(login_url='/accounts/login/')
def update_profile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
          return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
        else:
            form=ProfileForm()

    return render(request,'all-awards/profile_form.html',{"form":form}) 


def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_proTitle(search_term)
        message = f"{search_term}"

        return render(request, 'all-awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-awards/search.html',{"message":message})



# @login_required(login_url='/accounts/login/')
# def search_project(request):
#     try:

#         if 'project' in request.GET and request.GET["project"]:
#             search_term = (request.GET.get("project")).proTitle()
#             searched_project = Projects.objects.get(proTitle__icontains = searched_term.proTitle())
#             message = f"{search_term}"

#             return render(request, 'all-awards/search.html',{"message":message,"searched_project": searched_project})

#     except(ValueError,Projects.DoesNotExist):
#         raise Http404

#     return render(request,'all-awards/search.html')

