from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^new/profile', views.new_profile, name='new-profile'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^image/', views.projects, name='image'),
    url(r'^photo/(\d+)', views.photo, name='details'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)