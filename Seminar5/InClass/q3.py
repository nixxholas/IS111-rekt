def is_valid_username(username):
    # Ideally, we would want to stash all UTF-approved characters in a list for a precise and succinct check.
    return False if ((' ' in username) or (':' in username) or ('-' in username) or (username is '')
                     or (len(username) > 8) or any(x.isupper() for x in username)) else True


username_list = ['abcdefgh', 'abcdefghi', 'ab$cd', 'ab_cd', 'ab-cd', 'ab:cd', '', 'ab cd', 'abcDef', 'abc8ef']
for username in username_list:
    print("The username '" + username + "' is valid : " + str(is_valid_username(username)))
