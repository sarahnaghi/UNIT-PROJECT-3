from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index_view, name="index_view"),
        path('about/', views.about_view, name="about_view"),
        path('skills/', views.skills_view, name="skills_view"),


]