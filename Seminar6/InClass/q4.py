def retrieve_numbers(text):
    result = ""
    for i in range(len(text)):
        if text[i].isnumeric():
            result += text[i]
        elif not text[i].isnumeric() and len(result) > 0 and result[-1] != " ":
            result += " "

    return result


print(retrieve_numbers("12abc600$##0900AB 100X"))
print(retrieve_numbers("34.5689abc980"))
print(retrieve_numbers("xyz"))
print(retrieve_numbers("abc25xyz"))
