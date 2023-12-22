from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('upload/', views.upload,name='upload'),
    path('ezFile/',views.ez_FileList,name='ezFile'),
    path('ezFile/upload',views.ez_File_upload,name='ezFileUpload'),
]
  