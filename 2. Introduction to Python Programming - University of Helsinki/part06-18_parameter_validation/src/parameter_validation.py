# Creates and returns a tuple containing the data in the arguments.

def new_person(name: str, age: int):
    if name == "" or len(name.split(" ")) < 2 or len(name) > 40 or age < 0 or age >150:
        raise ValueError("Name not valid")
    return (name, age)
