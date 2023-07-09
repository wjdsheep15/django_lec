"""
URL configuration for my_project project.

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

from . import views




urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
    path('productlist/', views.productlist),
    path('productlist/detail/', views.productlist_detail),
    path('brand/', views.brand),
    path('brand/ph/', views.brand_ph),
    path('brand/cs/', views.brand_cs),

    path('login/signup/', views.login_signup),
    path('login/password_reset/', views.login_password_reset),
]
