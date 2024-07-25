from praktikum.burger import Burger
from unittest.mock import Mock, patch
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import random


class TestBurger:
    mock_available_buns = Mock()
    mock_available_buns.return_value = [Bun("black bun", 100),
                                        Bun("white bun", 200),
                                        Bun("red bun", 300)]

    mock_available_ingredients = Mock()
    mock_available_ingredients.return_value = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                                  Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                  Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                  Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

    def test_get_receipt(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        receipt = burger.get_receipt()

        assert ('(==== test_bun ====)') in receipt and first_ingredient.get_type().lower() in receipt and second_ingredient.get_type().lower() in receipt

    def test_set_bun(self):
        bun = random.choice(TestBurger.mock_available_buns())
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()

        assert bun.name in receipt

    def test_get_receipt_with_bun_only(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        burger = Burger()
        burger.set_buns(bun)
        receipt = burger.get_receipt()

        assert ('(==== test_bun ====)') in receipt

    def test_get_receipt_with_souse(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        receipt = burger.get_receipt()

        assert ('(==== test_bun ====)') in receipt and first_ingredient.get_type().lower() in receipt

    def test_get_receipt_with_filling(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        receipt = burger.get_receipt()

        assert ('(==== test_bun ====)') in receipt and first_ingredient.get_type().lower() in receipt

    def test_move_ingredient(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        first_ingredient_name = first_ingredient.get_name()
        second_ingredient_name = second_ingredient.get_name()
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        receipt = burger.get_receipt()
        first_index = receipt.find(first_ingredient_name)
        second_index = receipt.find(second_ingredient_name)
        burger.move_ingredient(0, 1)
        new_receipt = burger.get_receipt()

        assert burger.ingredients == [second_ingredient, first_ingredient]

    def test_remove_ingredient(self):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        receipt = burger.get_receipt()
        burger.remove_ingredient(0)
        new_receipt = burger.get_receipt()

        assert first_ingredient.get_name() not in new_receipt

    @patch('builtins.print')
    def test_print_receipt(self, mocked_print):
        bun_name = 'test_bun'
        bun = Bun(name=bun_name, price=12.5)
        first_ingredient = random.choice(TestBurger.mock_available_ingredients())
        second_ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        receipt = burger.get_receipt()

        assert ('(==== test_bun ====)') in receipt

    def test_get_price(self):
        bun = random.choice(TestBurger.mock_available_buns())
        ingredient = random.choice(TestBurger.mock_available_ingredients())
        burger = Burger()
        burger.set_buns(bun)
        burger_price = 2 * bun.get_price()
        burger.add_ingredient(ingredient)
        burger_price += ingredient.get_price()
        receipt_price = burger.get_price()

        assert receipt_price == burger_price