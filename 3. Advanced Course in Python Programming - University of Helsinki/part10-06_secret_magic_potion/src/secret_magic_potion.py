# Class for a magic potion.
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

#A SecretMagicPotion class which inherits the MagicPotion class and allows you to also protect the recipe with a password.            
class SecretMagicPotion(MagicPotion):
    # A constructor which also takes the password string as an argument.
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self.__password = password
        
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self.__password:
            super().add_ingredient(ingredient, amount)
        else:
            raise ValueError("Wrong password!")
            
    def print_recipe(self, password: str):
        if password == self.__password:
            super().print_recipe()
        else:
            raise ValueError("Wrong password!")
