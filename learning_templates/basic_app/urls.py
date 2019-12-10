from django.conf.urls import url
from django.contrib import admin
from basic_app import views
#TEMPLATE TAGGING

app_name = 'basic_app'


urlpatterns = [
    url(r'^other/$', views.other, name='other'),
    url(r'^rel_url/$', views.rel_url, name='rel_url'),
    #url(r'^base.html/$', views.base, name='')
]
