import random

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock


class TestIngredient:
    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                                               Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                               Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                               Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

    def test_get_type(self):
        ingredient = random.choice(TestIngredient.mock_available_ingredients())
        ingredient_type = ingredient.get_type()
        actually_type = ingredient.type

        assert ingredient_type == actually_type

    def test_get_name(self):
        ingredient = random.choice(TestIngredient.mock_available_ingredients())
        ingredient_name = ingredient.get_name()
        actually_name = ingredient.name

        assert ingredient_name == actually_name

    def test_get_price(self):
        ingredient = random.choice(TestIngredient.mock_available_ingredients())
        ingredient_price = ingredient.get_price()
        actually_price = ingredient.price

        assert ingredient_price == actually_price