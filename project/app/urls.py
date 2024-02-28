from django.urls import path,include
# from . import views
# urlpatterns = [
#     path("",views.RegisterPage,name="registerpage"),
#     path("register/",views.UserRegister,name="register"),
#     path("loginpage/",views.LoginPage,name="loginpage"),
#     path("loginuser/",views.LoginUser,name="login"),
# ]

from .views import *
urlpatterns = [
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
]