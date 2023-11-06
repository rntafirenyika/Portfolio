# Reads the contents of the file solutions.csv
# writes those lines which have a correct result into the file correct.csv
# writes those lines which have an incorrect result into the file incorrect.

def filter_solutions():
    # Reads the contents of the file solutions.csv
    sols = []
    with open("solutions.csv", "r") as file:
        for row in file:
            sols.append(row.strip().split(";"))

    correct = []
    incorrect = []
    for n in sols:
        if len(n[1].split("+")) == 2:
            q = n[1].split("+")
            if int(q[0]) + int(q[1]) == int(n[2]):
                correct.append(n)
            else:
                incorrect.append(n)
        elif len(n[1].split("-")) == 2:
            q = n[1].split("-")
            if int(q[0]) - int(q[1]) == int(n[2]):
                correct.append(n)
            else:
                incorrect.append(n)

    with open("correct.csv", "w") as file:
        for i in correct:
            for item in i:
                if item != i[-1]:
                    file.write(f"{item};")
                else:
                    file.write(f"{item}")
            file.write("\n")
    with open("incorrect.csv", "w") as file:
        for i in incorrect:
            for item in i:
                if item != i[-1]:
                    file.write(f"{item};")
                else:
                    file.write(f"{item}")
            file.write("\n")
