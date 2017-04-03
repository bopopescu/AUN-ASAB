from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.dashboard, name='dashboard')
]