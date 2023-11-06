#Takes a filename and a search string as its arguments.
#Goes through the file and select all recipes whose name contains the given search string.
def search_by_name(filename: str, word: str):
    recipes = {}
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            if line == "":
                recipes[recipe[0]] = recipe[1:]
                recipe = []
            else:
                recipe.append(line)
        recipes[recipe[0]] = recipe[1:]
    results = []
    for name in recipes:
        if name.lower().find(word.lower()) != -1:
            results.append(name)
    return results

#Takes a filename and an integer as its arguments.
#Goes through the file and select all recipes whose preparation time is at most the number given.
def search_by_time(filename: str, prep_time: int):
    recipes = {}
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            if line == "":
                recipes[recipe[0]] = recipe[1:]
                recipe = []
            else:
                recipe.append(line)
        recipes[recipe[0]] = recipe[1:]
    results = []
    for name, value in recipes.items():
        if int(value[0]) <= prep_time:
            results.append(f"{name}, preparation time {value[0]} min")
    return results

#Takes a filename and a search string as its arguments.
#Goes through the file and select all recipes whose ingredients contain the given search string.
def search_by_ingredient(filename: str, ingredient: str):
    recipes = {}
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            if line == "":
                recipes[recipe[0]] = recipe[1:]
                recipe = []
            else:
                recipe.append(line)
        recipes[recipe[0]] = recipe[1:]
    results = []
    for name, value in recipes.items():
        if ingredient in value:
            results.append(f"{name}, preparation time {value[0]} min")
    return results