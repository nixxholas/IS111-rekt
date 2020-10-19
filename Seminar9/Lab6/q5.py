def char_match(text, match):
    text_set = set(text)

    for c in text_set:
        if c not in match:
            return False

    return True


str1, str2 = " ", " "

while " " in str1 or " " in str2 or len(str2) < len(str1) or not char_match(str1, str2):
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    if " " in str1 or " " in str2 or len(str2) < len(str1) or not char_match(str1, str2):
        print("Conditions not satisfied!")
        print()

print()
print("Bingo!")
