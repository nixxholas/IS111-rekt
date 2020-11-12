def evaluate(expression):
    val = 0.0

    while True:
        m_index = get_nearest_operator_index(expression)
        left_val = ''
        right_val = ''

        if m_index > 0:
            for i in range(m_index - 1, -1, -1):
                if expression[i].isnumeric() or expression[i] == '.':
                    left_val += expression[i]
                else:
                    break
            left_val = left_val[::-1]

            for i in range(m_index + 1, len(expression)):
                if expression[i].isnumeric() or expression[i] == '.':
                    right_val += expression[i]
                else:
                    break
            computed = float(left_val) * float(right_val) if expression[m_index] == '*' else float(left_val) / float(
                right_val) if expression[m_index] == '/' else float(left_val) + float(right_val) if expression[
                                                                                                        m_index] == '+' else float(
                left_val) - float(right_val)

            expression = (expression[:m_index - len(left_val)] if (m_index - len(left_val)) > 0 else '') + str(
                computed) + (expression[m_index + len(right_val) + 1:] if m_index + len(right_val) + 1 < len(
                expression) else '')
        else:
            break

    return float(expression)


def get_nearest_operator_index(exp):
    for i in range(len(exp)):
        c = exp[i]
        if ('*' in exp or '/' in exp) and (c == '*' or c == '/'):
            return i
        elif '*' not in exp and '/' not in exp and (c == '+' or c == '-'):
            return i
    return -1
