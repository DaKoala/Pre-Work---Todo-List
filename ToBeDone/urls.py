"""ToBeDone URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from TodoList import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^index.html/$', views.index, name='finish'),
    url(r'^add.html/', views.add, name='add'),
    url(r'^\S+delete[0-9]+', views.delete, name='delete'),
    url(r'^delete[0-9]+', views.delete, name='delete'),
    url(r'^\S+edit[0-9]+', views.edit, name='edit'),
    url(r'^edit[0-9]+', views.edit, name='edit'),
    url(r'^\S+complete[0-9]+', views.complete, name='complete'),
    url(r'^complete[0-9]+', views.complete, name='complete'),
    url(r'^list_all.html/', views.list_all, name='list_all'),
    url(r'^list_prior.html/', views.list_prior, name='list_prior'),
    url(r'^list_expire.html/', views.list_expire, name='list_expire'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
