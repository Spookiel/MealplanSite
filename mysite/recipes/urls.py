from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "recipes"
urlpatterns = [
    path('', views.recipe_list, name="recipe_list"),
    path("details/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
]