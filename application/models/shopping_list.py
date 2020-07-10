from application.models.recipes import get_recipe_by_id
from typing import List
import pandas as pd
from application import app


class ShoppingList:
    def __init__(self):
        self.recipes = List[int]
        self.ingredients = List[dict]

    def add_recipe(self, recipe_id: int):
        self.recipes.append(recipe_id)
        return recipe_id

    def remove_recipe(self, recipe_id: int):
        self.recipes.remove(recipe_id)
        return recipe_id

    def add_recipe_ingredients_to_list(self, gender='male', location='AU'):
        for recipe_id in self.recipes:
            recipe_data = self.get_recipe_ingredients(recipe_id)
            if not recipe_data:
                return False
            ingredients = next((recipe for recipe in recipe_data
                                if recipe["gender"] == gender and recipe['country'] == location), False)
            self.ingredients.append(ingredients)
        return True

    @staticmethod
    def get_recipe_ingredients(recipe_id: int) -> dict:
        recipe_data = get_recipe_by_id(recipe_id).get('recipe_data')
        return recipe_data

