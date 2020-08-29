import lab_2_util
# ################################################################################
# The following code is given to you.
def q7_1(str1, str2, str3):
    """
    This function takes in 3 strings str1, str2 and str3, and returns 
    a string that contains the common characters shared by str1, str2 
    and str3. If a character appears more than once in str1, str2, or 
    str3, it will only appear once in the returned string.
    
    You are expected to use the get_common_characters() function from 
    lab_2_util.py to help you implement this function.
    
    For example, if str1 is "ABBCDE", str2 is "ABBC" and str3 is "ABBD",
    then this function should return "AB".
    """
    # Modify the code below to return a correct string.
    return lab_2_util.get_common_characters(lab_2_util.get_common_characters(str1, str2), str3)
    
    
def q7_2(str1, str2, str3):
    """
    This function takes in 3 strings str1, str2 and str3, and returns 
    a string that contains the characters that satisfy the following 
    two conditions:
        - The character must be contained in str1.
        - The character must be contained in either str2 or str3.
    
    For example, if str1 is "ABCDE", str2 is "ABC" and str3 is "ABD",
    then this function should return "ABCD".
    """
    # Modify the code below to return a correct string.
    
    return lab_2_util.get_common_characters(str1, str2 + str3)

# The code below is for testing the functions. Do not modify the code below.

s1 = "singapore management university"
s2 = "school of information systems"
s3 = "python"

print(q7_1(s1, s2, s3))
print(q7_2(s1, s2, s3))

