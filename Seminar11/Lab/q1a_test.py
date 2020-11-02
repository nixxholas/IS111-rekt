from q1a import encrypt

# Test cases used to test your function

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
print("Expected: v ybir clguba")
msg = 'i love python'
print("Actual  : " + encrypt(cipher_dict, msg))