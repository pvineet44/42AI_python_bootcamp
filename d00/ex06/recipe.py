import sys

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


def print_recipe():
    """prints a recipe from cookbook"""
    recipe = input("Please enter the recipe's name to get its details:\n")
    ingredients = cookbook.get(recipe).get('ingredients')
    meal = cookbook.get(recipe).get('meal')
    prep_time = cookbook.get(recipe).get('prep_time')
    print("Recipe for " + recipe + " : ")
    print("Ingredients list:" + str(ingredients))
    print("To be eaten for " + str(meal) + ".")
    print("Takes " + str(prep_time) + " minutes of cooking.")


def add_recipe():
    """adds recipe to the cookbook"""
    recipe = input("Please enter the recipe name\n")
    cookbook[recipe] = {}
    cookbook[recipe]['time'] = input("Enter time required to cook\n")
    cookbook[recipe]['type'] = input("Enter type of recipe(eg:lunch)\n")


def delete_recipe():
    """deletes recipe from the cookbook"""
    recipe = input("Please enter the recipe name to delete")
    cookbook.pop(recipe)


while (True):
    print("Please select an option by typing the corresponding number:")
    print("1. Add a recipe")
    print("2. Delete a recipe")
    print("3. Print a recipe")
    print("4. Print the cookbook")
    print("5. Quit")
    respone = input()
    if (respone == '1'):
        add_recipe()
    if (respone == '2'):
        delete_recipe()
    if (respone == '3'):
        print_recipe()
    if (respone == '4'):
        print(cookbook)
    if (respone == '5'):
        print("Cookbook closed.")
        sys.exit(0)
    else:
        print("This option does not exist,'\
            'please type the corresponding number.")
        print("To exit, enter 5")
