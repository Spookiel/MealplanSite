from django.shortcuts import render

# Create your views here.

from .models import Recipe

def recipe_list(request):

    recipes = Recipe.objects.all()

    context = {"recipes":recipes}

    return render(request, "recipes/all_recipes.html", context)