class   Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """instantiates the object with values"""
        self.name = str(name)
        assert(self.name != "")
        self.cooking_lvl = int(cooking_lvl)
        assert(self.cooking_lvl in range(5))
        self.cooking_time = int(cooking_time)
        assert(self.cooking_time > 0)
        self.ingredients = list(ingredients)
        assert(self.ingredients)
        self.recipe_type = str(recipe_type)
        assert(self.recipe_type == 'lunch' \
        or self.recipe_type =='dinner' or \
                  self.recipe_type == 'dessert')
        self.description = description


    def __str__(self):
        """Return the string to print with recipe info"""
        txt = ""
        txt = "Recipe name: " + self.name + " Cooking level: " \
        + str(self.cooking_lvl) + " Cooking time: " + str(self.cooking_time)\
        + " Ingredients: " + str(self.ingredients) + " Description: " + str(self.description)\
            + " Recipe type: " + str(self.recipe_type)
        return txt