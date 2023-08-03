from django.db import models
from django.contrib import auth
from datetime import timedelta
from django.utils import timezone

def in_three_days():
    return timezone.now() + timedelta(days=3)

class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    packetQuantityGrams = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    instructions = models.CharField(max_length=5000, default="No detailed Instructions")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    rname = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    iname = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipeQuantityGrams = models.DecimalField(max_digits=8, decimal_places=4, default=0)

class StorageUnit(models.Model):
    ### Stores cupboard and fridge items
    owner = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='StorageIngredient')

class StorageIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    isFridge = models.BooleanField(default=False)
    stored_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=in_three_days)
    