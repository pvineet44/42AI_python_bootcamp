from recipe import Recipe
from book import Book
from datetime import datetime

cookbook = {
             'sandwich':
             {
                 'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                 'meal': 'lunch',
                 'prep_time': '10 minutes'
             },
             'cake':
             {
                 'ingredients': ['flour, sugar, eggs'],
                 'meal': 'dessert',
                 'prep_time': '60 minutes'
             },
             'salad':
             {
                 'ingredients': ['avocado, arugula, tomatoes, spinach'],
                 'meal': 'lunch',
                 'prep_time': '15 minutes'
             }
            }


r1 = Recipe("paratha", 4, 10, ['curd','milk','maida'],'','lunch')
to_print = str(r1)
print(to_print)

b1 = Book('Recipe-Book', cookbook)

r2 = b1.get_recipe_by_name('cake')
#r3 = b1.get_recipes_by_types('lunch')
b1.add_recipe(r1)
r2 = b1.get_recipe_by_name('paratha')
print(r2)

