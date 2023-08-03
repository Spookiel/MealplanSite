from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Recipe, RecipeIngredient

def recipe_list(request):

    recipes = Recipe.objects.all()
    rdetails = {}
    for recipe in recipes:
        #print(recipe.name, "HERE WITH ID", recipe.id)
        res = RecipeIngredient.objects.all()
        # for i in res:
        #     print("FOUND Ingredient", i.rname, i.iname, i.recipeQuantityGrams)
        rdetails[recipe] = res
        
    context = {"recipes":recipes, "rdetails":rdetails}

    return render(request, "recipes/all_recipes.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe":recipe})