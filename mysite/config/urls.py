"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from news.views import base_views as views_news  # news app 하위에 views를 Import.

## 장고 프로젝트에서 url 해석을 위해 가장 최초로 접근하는 모듈. (urls.py)

urlpatterns = [
    path("", views_news.index),
    path("admin/", admin.site.urls),
    path("common/", include("common.urls")),
    path("news/", include("news.urls")),
]
