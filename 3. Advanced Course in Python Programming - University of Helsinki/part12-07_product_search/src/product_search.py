#Returns a new list containing those tuples from the original which fulfil the criterion(own function which takes a function as its argument).
def search(products: list, criterion: callable):
    return [i for i in products if criterion(i)]
