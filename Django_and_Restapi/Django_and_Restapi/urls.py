"""rest322 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from testapp import views

from rest_framework import routers
router=routers.DefaultRouter()
router.register('api', views.EmployeeCRUD)

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^List/',views.EmployeeListAPIView.as_view()),
    # example http://127.0.0.1:8000/List/?search=swami
    
    
    
    url(r'',include(router.urls)),
    # example http://127.0.0.1:8000/api/

     url(r'^auth-jwt/',obtain_jwt_token),
     url(r'^auth-jwt-refresh/',refresh_jwt_token),
     url(r'^auth-jwt-verify/',verify_jwt_token),

    # for jwt token authtoken


]
