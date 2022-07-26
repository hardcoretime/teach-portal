"""teachportal URL Configuration

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

from courses import views
from courses.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    ScheduleListView, ScheduleDetailView
from teachportal.settings import DEBUG

urlpatterns = [
    path('', views.index, name='main'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    path('course/update/<int:pk>', CourseUpdateView.as_view(), name='course_update'),
    path('course/delete/<int:pk>', CourseDeleteView.as_view(), name='course_delete'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('schedules/', ScheduleListView.as_view(), name='schedules'),
    path('admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
