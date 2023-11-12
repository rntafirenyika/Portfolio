#Using list comprehensions with own classes
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration

# Takes a ShoppingList object and an integer value as its arguments.
# Returns a list of product names that includes only the products with at least the number of items specified by the amount parameter.
def products_in_shopping_list(shopping_list, amount: int):
    return [i[0] for i in shopping_list if i[1] >= amount]