


from django.contrib import admin
from django.urls import path, include
from .views import tracker_index


app_name = "tracker"

urlpatterns = [path('', tracker_index, name="tracker_index")]