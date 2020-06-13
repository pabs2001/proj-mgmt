from django.urls import path
from hello_projects import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello_projects/<name>", views.hello_there, name="hello_there"),
]