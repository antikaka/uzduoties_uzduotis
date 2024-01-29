"""
URL configuration for mysite project.

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
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register", views.register, name="register"),
    path("uzduotys", views.UzduotysListView.as_view(), name="uzduotys"),
    path("<int:uzduotis_id>", views.viena_uzduotis, name="uzduotis"),
    path("uzduota_uzduotis", views.UzduotisCreateView.as_view(), name="uzduotis_nauja"),
    path('tinymce/', include('tinymce.urls')),
    path("<int:pk>/update", views.UzduotisUpdateView.as_view(), name="uzduotis_pakeista"),
    path("<int:pk>/delete", views.UzduotisDeleteView.as_view(), name="istrinta_uzduotis"),

]
