from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('upload/', views.upload,name='upload'),
    path('ezFile/',views.ez_FileList,name='ezFile'),
    path('ezFile/upload',views.ez_File_upload,name='ezFileUpload'),
    path('ezFile/login',views.login_user,name='login'),
    path('ezFile/logout',views.logout_user,name='logout'),
    path('ezFile/signup',views.signup,name='signup'),
    #path('verification/',include('verify_email.urls')),
    #uncomment to integrate email verification
]
  