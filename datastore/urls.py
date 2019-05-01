"""datastore URL Configuration

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from userauth.views import User_register_view, delete_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datacollector_app.urls')),
    path('register/', User_register_view.as_view(), name='datastore-register'),
    path('login/', auth_views.LoginView.as_view(template_name='userauth/login.html'), name='datastore-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userauth/logout.html'),
         name='datastore-logout'),
    path('delete/', delete_account, name='datastore-user-delete')
]
