from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name