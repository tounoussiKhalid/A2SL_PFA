"""A2SL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.splash_view,name='splash'),

    path('home/',views.home_view,name='home'),

    path('admin/', admin.site.urls),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('animation/',views.animation_view,name='animation'),
    path('totext/home',views.totext_home_view,name='totext/home'),
    path('totext/collecte',views.totext_collecte,name='totext/collecte'),
    path('totext/training',views.totext_training,name='totext/training'),
    path('totext/prediction',views.totext_prediction,name='totext/prediction'),

]
