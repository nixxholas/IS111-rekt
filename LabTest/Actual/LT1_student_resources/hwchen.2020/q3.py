# Name:
# Email ID:

import string


def check_math(list_of_equations):
    """
    list_of_equations: List of strings where each string is a math eqn,
    always consists of an integer, an operator and another integer.
    """
    if len(list_of_equations) < 1: return True

    # Iterate every equation
    for eqn in list_of_equations:
        first_val = None
        eqn_symbol = None
        second_val = None
        equal_found = False
        final_res = None

        # Convert the eqn to a list first
        eqn_chars = list(eqn)
        for c in eqn_chars:
            if c != " ":
                if c.isnumeric():
                    # If the equation symbol is not found yet, we still tryna fill up the number.
                    if eqn_symbol is None:
                        first_val = int(c) if first_val is None else int(str(first_val) + c)
                    elif not equal_found:
                        second_val = int(c) if second_val is None else int(str(second_val) + c)
                    else:
                        final_res = int(c) if final_res is None else int(str(final_res) + c)
                elif not c.isnumeric() and c not in string.ascii_letters:
                    if eqn_symbol is None and c != "=":
                        eqn_symbol = c
                    elif c != "=" and len(eqn_symbol) < 2:
                        eqn_symbol += c
                    elif c == "=":
                        equal_found = True

        if first_val is None or second_val is None or eqn_symbol is None or final_res is None:
            return False
        else:
            if eqn_symbol == "*":
                if (first_val * second_val) != final_res:
                    return False
            elif eqn_symbol == "/":
                if (first_val / second_val) != final_res:
                    return False
            elif eqn_symbol == "//":
                if (first_val // second_val) != final_res:
                    return False
            elif eqn_symbol == "%":
                if (first_val % second_val) != final_res:
                    return False
            elif eqn_symbol == "+":
                if (first_val + second_val) != final_res:
                    return False
            elif eqn_symbol == "-":
                if (first_val - second_val) != final_res:
                    return False
            else:
                return False

        return True
