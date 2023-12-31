"""
URL configuration for Tumbleweed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path 
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/', views.about_page, name='about'),
    path('companies/', views.companies_page, name='companies'),
    path('contact/', views.contact, name='contact'),
    path('openings/details/<uuid:pk>/', views.opening_details.as_view(), name='opening-details'),
    path('compannies/search', view=views.companies_search_page, name="sector_filter"),
    path('statistics', views.CompanyJsonView.as_view(), name="companies-json")
]

