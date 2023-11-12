class LotteryNumbers:
    # Constructor that takes the week number (an integer value) and a list of seven integers as arguments.
    def __init__(self, week_num: int, lott_numbers: list):
        self.__week_num = week_num
        self.__lott_numbers = lott_numbers
    
    # Returns the number of correct entries in the parameter list.    
    def number_of_hits(self, numbers: list):
        return len([i for i in numbers if i in self.__lott_numbers])
    
    # Returns a new list of seven integers which contains only those items from the original list which match the week's correct numbers with -1 in place of the incorrect numbers.        
    def hits_in_place(self, numbers: list):
        return [i if i in self.__lott_numbers else -1 for i in numbers]
