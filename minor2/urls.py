"""minor2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from minor2 import views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quiz/',views.quiz.as_view()),
    url(r'^auth/',views.authentication.as_view()),
    url(r'^batchdetails/',views.batchdetails.as_view()),
    url(r'^api/', include('fileupload_rest.urls') ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns=format_suffix_patterns(urlpatterns)
