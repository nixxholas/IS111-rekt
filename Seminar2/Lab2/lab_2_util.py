# This function is given to you

def get_common_characters(str1, str2):
    """
    This function takes in two string parameters, namely str1 and str2, and returns
    a string containing all the characters in str1 that also appear in str2.
    
    Note that if a character appears more than once in str1 and it appears in str2, 
    the character will only appear once i--n the returned string.
    """
    result = ""
    for ch in str1:
        if (ch in str2) and (not (ch in result)):
            result = result + ch
    return result