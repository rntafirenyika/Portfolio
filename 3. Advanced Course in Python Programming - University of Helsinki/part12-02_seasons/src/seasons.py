#Takes a list of dictionaries as its argument. Sorts by the number of seasons each show has, in ascending order, and returns a new list.
def sort_by_seasons(items: list):
    def order_by_num(item: dict):
        return item["seasons"]
    
    return sorted(items, key=order_by_num)