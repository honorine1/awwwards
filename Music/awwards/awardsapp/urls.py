from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^project_posts/', views.project_posts, name='project_posts'),
    url(r'^new_post/',views.new_post,name='new_post'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^update_profile/(\d+)',views.update_profile,name = 'update_profile'),
    url(r'^search/',views.search_project,name = 'search_project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)