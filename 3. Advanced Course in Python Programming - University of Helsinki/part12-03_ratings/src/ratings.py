#Takes a list of dictionaries as its argument. Sorts the dictionaries in descending order based on the shows' ratings and returns a new list.
def sort_by_ratings(items: list):
    def order_by_rating(item: dict):
        return item["rating"]
    
    return sorted(items, key=order_by_rating, reverse=True)