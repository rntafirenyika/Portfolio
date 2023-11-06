#Own programming language executor.
#PRINT [value]: prints the value
#MOV [variable] [value]: assigns the value to the variable
#ADD [variable] [value]: adds the value to the variable
#SUB [variable] [value]: subtracts the value from the variable
#MUL [variable] [value]: multiplies the variable by the value
#[location]:: names a line of code, so it can be jumped to from elsewhere
#JUMP [location]: jumps to the location specified
#IF [condition] JUMP [location]: if the condition is true, jump to the location specified
#END: finish execution

def comp(entries: list, int1, int2):
    if entries[2] == "==":
        return (int1 == int2, entries[5])
    elif entries[2] == "<=":
        return (int1 <= int2, entries[5])
    elif entries[2] == ">=":
        return (int1 >= int2, entries[5])
    elif entries[2] == "!=":
        return (int1 != int2, entries[5])
    elif entries[2] == "<":
        return (int1 < int2, entries[5])
    elif entries[2] == ">":
        return (int1 > int2, entries[5])

def indices(commands: list):
    results = {}
    for i in range(len(commands)):
        if commands[i].endswith(":"):
            results[commands[i][0:-1]] = i
    return results

def run(program: list):
    variables = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
    jump_to = indices(program)
    results = []
    length = len(program)
    i = 0
    while i < length:
        try:
            substrings = program[i].split()
            instr = []
            for substring in substrings:
                try:
                    integer_value = int(substring)
                    instr.append(integer_value)
                except ValueError:
                    instr.append(substring)
        except AttributeError:
            continue

        if instr[0] == "PRINT":
            if type(instr[1]) == str:
                results.append(variables[instr[1]])
            else:
                results.append(instr[1])
        elif instr[0] == "MOV":
            if isinstance(instr[2], str):
                variables[instr[1]] = int(variables[instr[2]])
            else:
                variables[instr[1]] = instr[2]
        elif instr[0] == "ADD":
            if isinstance(instr[2], str):
                variables[instr[1]] += int(variables[instr[2]])
            else:
                variables[instr[1]] += instr[2]
        elif instr[0] == "SUB":
            if isinstance(instr[2], str):
                variables[instr[1]] -= int(variables[instr[2]])
            else:
                variables[instr[1]] -= instr[2]
        elif instr[0] == "MUL":
            if isinstance(instr[2], str):
                variables[instr[1]] *= int(variables[instr[2]])
            else:
                variables[instr[1]] *= instr[2]
        elif instr[0] == "JUMP":
            i = jump_to[instr[1]]
        elif instr[0] == "IF":
            if type(instr[3]) == str:
                result, jump = comp(instr, variables[instr[1]], variables[instr[3]])
            else:
                result, jump = comp(instr, variables[instr[1]], instr[3])
            if result:
                i = jump_to[jump]
        elif instr[0] == "END":
            break
        with open("info.txt", 'a') as file:
            file.write(f"{i} {results} {instr} {variables}\n")
        i += 1
    return results
