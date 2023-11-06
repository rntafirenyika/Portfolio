# Takes a list of tuples as its argument.
# Finds the oldest person on the list and return their name.

def oldest_person(people: list):
    smallest = ""
    for person in people:
        if smallest == "" or person[1] < smallest:
            smallest = person[1]
    for person in people:
        if person[1] == smallest:
            return person[0]