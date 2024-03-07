"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",RegisterPage,name="registerpage"),
    path("register/",UserRegister,name="register"),
    path("loginpage/",LoginPage,name="loginpage"),
    path("loginuser/",LoginUser,name="login"),
    path("insert/<str:pk>",query,name="query"),
    path('showpage/<str:pk>',showdata,name='showdata'),
    path('editpage/<int:pk>/',editPage,name='editpage'),
    path('update/<int:pk>/',updateData,name='update'),
    path('delete/<int:pk>/',deleteData,name='delete'),
    path('search/<str:pk>',search,name='search'),
    path('logout/',logout,name='logout')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
