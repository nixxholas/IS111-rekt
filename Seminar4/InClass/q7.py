def is_palindrome(txt):
    for i in range(0, len(txt)):
        if txt[i] != txt[len(txt) - (i + 1)]: return False
    return True


word = input("Enter a word: ")
print(word, "is" if is_palindrome(word) else "is not", "a palindrome.")
