from django.db import models


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
