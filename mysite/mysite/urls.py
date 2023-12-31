"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from recipes.views import recipe_list, recipe_detail, index, storage_index
from accounts.views import login, register, logout

app_name = "MANAGER"
urlpatterns = [
    path('', index, name="index"), ## include('recipes.urls')
    path('recipes', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path("meal-tracker", include('tracker.urls')),
    path("storage", storage_index, name="storage-index")
]
