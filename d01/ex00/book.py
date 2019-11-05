from datetime import datetime
class Book:
    def __init__(self, name, recipes_list):
        self.name = str(name)
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.recipes_list = dict(recipes_list)


    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if name in self.recipes_list:
            print(self.recipes_list.get(name))
            return(self.recipes_list.get(name))
    
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipes ={}
        for recipe in self.recipes_list:
            if (recipe_type == recipe.recipe_type):
                recipes.update({recipe.name: recipe})
        return recipes
    
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        rl = dict(self.recipes_list)
        rl.update({recipe.name: recipe})
        now = datetime.now()
        self.last_update = now.strftime("%d/%m/%Y %H:%M:%S")

