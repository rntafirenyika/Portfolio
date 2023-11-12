# Person class
class Person:
    def __init__(self, name: str):
        self.name = name

    # Returns the first name of the person        
    def return_first_name(self):
        first_name = self.name.split()[0]
        return first_name

    # Returns the last name of the person        
    def return_last_name(self):
        last_name = self.name.split()[1]
        return last_name
        
        
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())
        