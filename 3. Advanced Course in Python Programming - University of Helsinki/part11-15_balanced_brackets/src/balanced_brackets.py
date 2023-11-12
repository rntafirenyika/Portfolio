# Takes a string as its argument.
# Checks if the round brackets, or parentheses, within the string are balanced.
# That is, for each opening bracket ( there should be a closing bracket ), and all pairs of brackets should be matched in order.
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if my_string[0] == ')' or my_string[0] == ']':
        return False
    if not (my_string[0] == '(' or my_string[0] == '['):
        return balanced_brackets(my_string[1:])
    elif my_string[0] == '(':
        if my_string[-1] == ')':
            return balanced_brackets(my_string[1:-1])
        elif len(my_string) == 1:
            return False
        else:
            return balanced_brackets(my_string[:-1])
    elif my_string[0] == '[':
        if my_string[-1] == ']':
            return balanced_brackets(my_string[1:-1])
        elif len(my_string) == 1:
            return False
        else:
            return balanced_brackets(my_string[:-1])