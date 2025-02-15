"""bira URL Configuration

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
from django.urls import re_path as url
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="docs")),

    path('admin/', admin.site.urls),
    path('api/v1/', include('apis.urls')),
    path('docs/', include_docs_urls(title='BIRA API v1'), name='api_docs'),

]
