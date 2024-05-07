"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from modulos.views import first_view,second_view,third_view,four_view,five_view,six_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', first_view, name='login'),
    path('index/', second_view, name='index'),
    path('rec1/', third_view, name='rec1'),
    path('rec2/', four_view, name='rec2'),
    path('rec3/', five_view, name='rec3'),
    path('cal_sug/', six_view, name='cal_sug'),
]
