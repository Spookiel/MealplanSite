from django.shortcuts import render

# Create your views here.

from .models import Recipe, RecipeIngredient

def recipe_list(request):

    recipes = Recipe.objects.all()
    rdetails = {}
    for recipe in recipes:
        print(recipe.name, "HERE")
        res = RecipeIngredient.objects.all()
        for i in res:
            print("FOUND Ingredient", i.rname, i.iname, i.recipeQuantityGrams)
        rdetails[recipe.name] = res
    context = {"recipes":recipes, "rdetails":rdetails}

    return render(request, "recipes/all_recipes.html", context)