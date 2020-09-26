# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

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
                    # If the equal symbol is not found yet, we still tryna fill up the number.
                    elif not equal_found:
                        second_val = int(c) if second_val is None else int(str(second_val) + c)
                    # If the equation is not ending yet, we still tryna fill up the number.
                    else:
                        final_res = int(c) if final_res is None else int(str(final_res) + c)
                elif not c.isnumeric() and c not in string.ascii_letters:
                    # Since its not numeric and not letter-based, its most likely a symbol
                    if eqn_symbol is None and c != "=":
                        # Make sure its not = so that we can assume its an arithmetic
                        # operation with a much higher precision.
                        eqn_symbol = c
                    elif c != "=" and len(eqn_symbol) < 2:
                        # Since eqn_symbol may be a //, we let it in if its not an =
                        eqn_symbol += c
                    elif c == "=" and not equal_found:
                        # Since this is an =, we sort this out as an equal found.
                        equal_found = True
                    else:
                        # If we have a duplicate symbol or something, we terminate immediately.
                        return False

        # If any of the arithmetic conditions are not met,
        if first_val is None or second_val is None or eqn_symbol is None or final_res is None:
            return False
        else:
            # Else we can safely assume its more or less an arithmetic operation
            # Condition 1: Ensure its a proper arithmetic operation
            # Condition 2: Ensure the operation always == final_res
            # If these are not met, return False and stop immediately, no need to continue.
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
            # Invalid symbol, don't test my patience lol.
            else:
                return False

        return True
