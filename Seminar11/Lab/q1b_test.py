from q1b import decrypt

cipher_dict = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}

print('\nTestcase')
print('-' * 10)
msg = 'v ybir clguba'
print("Expected: i love python")
print("Actual  : " + decrypt(cipher_dict, msg))