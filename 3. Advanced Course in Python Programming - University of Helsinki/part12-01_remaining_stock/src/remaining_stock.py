#Takes a list of tuples as its argument. Return a new list, where the items are sorted according to the stock remaining, lowest value first.
def sort_by_remaining_stock(items: list):
    def order_by_stock(item: tuple):
        return item[2]
    
    return sorted(items, key=order_by_stock)