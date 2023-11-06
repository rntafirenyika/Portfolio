# Takes a tuple containing some identifying information as its argument.
# The information is processed and written/appended into the file people.csv.

def store_personal_data(person: tuple):
    with open("people.csv", "a") as file:
        entry = ""
        for data in person:
            if type(data) == float or type(data) == int:
                data = str(data)
            if data == str(person[-1]):
                entry += f"{data}\n"
            else:
                entry += f"{data};"
        file.write(entry)