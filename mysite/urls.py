"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from schoolbridge import views 


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/<int:pk>/', views.announcement_detail, name='announcement_detail'),
    path('tasks/', views.task_list, name='task_list'),
    path('gradebook/', views.gradebook, name='gradebook'),
    path('file-upload/', views.file_upload, name='file_upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/<int:pk>/', views.file_detail, name='file_detail'),
]

