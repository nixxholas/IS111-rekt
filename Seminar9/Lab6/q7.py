def get_lineup(order):
    final_order = []

    while len(order) > 0:
        el = order.pop(0)

        if el[1] == "":
            final_order.append(el[0])
        else:
            inserted = False

            for i in range(len(final_order)):
                if final_order[i] == el[0] and (i + 1 == len(final_order) or final_order[i + 1] != el[1]):
                    final_order.insert(i, el[1])
                    inserted = True
                elif final_order[i] == el[1] and (i - 1 < 0 or final_order[i - 1] != el[0]):
                    final_order.insert(i, el[0])
                    inserted = True

            if not inserted:
                order.append(el)

    return final_order


print(get_lineup([("Chris", "Darren"), ("Alice", "Bob"), ("Darren", ""), ("Bob", "Chris")]))
print(get_lineup([("Mary", "Jason"), ("John", "Alan"), ("Jason", "George"), ("Alan", "Christie"), ("Christie", "Mary"),
                  ("George", "")]))
