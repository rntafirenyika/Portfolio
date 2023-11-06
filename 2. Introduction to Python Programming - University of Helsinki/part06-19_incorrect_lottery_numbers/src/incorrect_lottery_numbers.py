# Creates a file called correct_numbers.csv. The file contains only those lines from the original file which are in the correct format.
# The correct format contains a header "week x", followed by seven integer numbers which are all between 1 and 39 inclusive.

def filter_incorrect():
    with open("lottery_numbers.csv", "r") as file, open("correct_numbers.csv", "w") as correct:
        for row in file:
            parts = row.strip().split(";")
            week_num = (parts[0].split(" "))[1]
            numbers = parts[1].split(",")
            try:
                week_num = int(week_num)
                for number in numbers:
                    number = int(number)
                    if number > 39 or number < 1 or len(numbers) != 7 or numbers.count(str(number)) > 1:
                        raise ValueError
            except ValueError:
                continue
            correct.write(row)
