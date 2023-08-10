from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Recipe, RecipeIngredient, StorageUnit


def recipe_list(request):

    recipes = Recipe.objects.all()
    rdetails = {}
    for recipe in recipes:
        #print(recipe.name, "HERE WITH ID", recipe.id)
        res = RecipeIngredient.objects.filter(rname=recipe.id)
        # for i in res:
        #     print("FOUND Ingredient", i.rname, i.iname, i.recipeQuantityGrams)
        rdetails[recipe] = res
        #print(res, recipe.name)
        
    context = {"recipes":recipes, "rdetails":rdetails}

    return render(request, "recipes/all_recipes.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe":recipe})

def index(request):

    context = {}
    return render(request, "recipes/index.html", context)

def meal_planner(request):
    return render(request, "BLAH")

def storage_index(request):
    store_units = StorageUnit.objects.filter(owner=request.user)
    assert len(store_units) == 1
    store_unit = store_units[0]
    fridge_ings = store_unit.ingredients.filter(storageingredient__isFridge=True)
    print(fridge_ings)
    print(store_unit)
    context = {"fridge_ings":fridge_ings}




    return render(request, "storage/index.html", context)