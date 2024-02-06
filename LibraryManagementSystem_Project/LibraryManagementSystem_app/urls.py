from django.urls import path
from LibraryManagementSystem_app import views

urlpatterns = [
  path("" , views.home , name="home"),
]