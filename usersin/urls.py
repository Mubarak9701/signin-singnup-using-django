from django.urls import path
from usersin import views

urlpatterns = [
    path('', views.home,name="home"),
    path('register/',views.register,name="register"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
]