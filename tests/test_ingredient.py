from praktikum.ingredient import Ingredient
from data import name_ingredient, price_ingredient, ingredient_type


class TestIngredient:

    def test_get_price_ingredient(self):
        ingredient = Ingredient(ingredient_type, name_ingredient, price_ingredient)
        assert ingredient.get_price() == price_ingredient

    def test_get_name_ingredient(self):
        ingredient = Ingredient(ingredient_type, name_ingredient, price_ingredient)
        assert ingredient.get_name() == name_ingredient

    def test_get_type_ingredient(self):
        ingredient = Ingredient(ingredient_type, name_ingredient, price_ingredient)
        assert ingredient.get_type() == ingredient_type
