from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^new/profile', views.new_profile, name='new-profile'),
    url(r'^profile/', views.profile, name='profile'),
]