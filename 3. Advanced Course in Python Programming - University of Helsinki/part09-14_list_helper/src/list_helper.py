#class with class methods
class ListHelper:
    # Returns the most common item on the list.
    @classmethod
    def greatest_frequency(cls, my_list: list):
        unique = set(my_list)
        count = 0
        most_common = None
        for num in unique:
            if my_list.count(num) > count:
                count = my_list.count(num)
                most_common = num
        return most_common

    # Returns the number of unique items which appear at least twice on the list.
    @classmethod
    def doubles(cls, my_list: list):
        unique = set(my_list)
        count = 0
        for num in unique:
            if my_list.count(num) > 1:
                count += 1
        return count