"""Sviluppatori URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from navbar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.first_page),
    url(r'^sign_up', views.sign_up_page),
    url(r'^contact_us', views.contact_us),
    url(r'^contacted', views.contacted),
    url(r'^login', views.log_in),
    url(r'^logout', views.log_out),
    url(r'^panel', views.panel),
    url(r'^profile', views.profile),
    url(r'^user_edit', views.user_edit),
]
