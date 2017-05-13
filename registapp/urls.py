"""registapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views
#import captcha

urlpatterns = [
    url(r'^$', views.index),
    url(r'^poll/(\d+)$', views.poll, name='poll-url'),
    url(r'^vote/(\d+)/(\d+)$', views.vote, name='vote-url'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    #for delete: (id)(user_pass) = arg => def index(request, pid=None, del_pass=None):
    #url(r'^(\d+)/(\w+)/$', views.index),
    #url(r'^userinfo/$', views.userinfo),
    #url(r'^post/$', views.posting),
    #url(r'^login/$', views.login),
    #url(r'^logout/$', views.logout),
    #url(r'^captcha/', include('captcha.urls')),
    #url(r'^accounts/', include('registration.backends.hmac.urls')),
]
