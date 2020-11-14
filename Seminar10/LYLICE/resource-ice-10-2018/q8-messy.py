
def rot (sentence, offset):                        
    result = ''                        
    for ch in sentence:
        if ch == ' ':
            result     += ' '
        else:
            result += chr( (ord(ch)     -   ord('a') + offset) % 26                                   + ord('a'))            

    return                          result

print (rot('xyz',2))
