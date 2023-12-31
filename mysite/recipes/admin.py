from django.contrib import admin

# Register your models here.

from .models import Ingredient, Recipe, RecipeIngredient, StorageUnit, StorageIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(StorageUnit)
admin.site.register(StorageIngredient)